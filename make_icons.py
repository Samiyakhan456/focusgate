#!/usr/bin/env python3
"""
make_icons.py — Generates the PNG icons needed by the Chrome extension.
Run once from the focusgate/ folder:  python make_icons.py
No external libraries required — uses only Python's built-in modules.
"""

import os, struct, zlib

def make_png(size, path):
    bg  = (245, 240, 232)   # cream background
    acc = (232,  80,  42)   # coral accent

    pixels = []
    cx, cy = size // 2, size // 2

    for y in range(size):
        row = []
        for x in range(size):
            nx, ny = x - cx, y - cy

            # Body of padlock: rounded rect in lower 55%
            bw = int(size * 0.50)
            bh = int(size * 0.38)
            bx0, bx1 = cx - bw//2, cx + bw//2
            by0, by1 = cy - int(size*0.06), cy + bh

            # Shackle: half-circle arc on top
            shackle_cy  = cy - int(size * 0.12)
            shackle_r   = int(size * 0.20)
            shackle_t   = max(2, int(size * 0.09))
            dist = ((nx)**2 + (y - shackle_cy)**2) ** 0.5
            in_shackle = (
                abs(dist - shackle_r) < shackle_t and
                y <= shackle_cy and
                x >= bx0 + shackle_t and
                x <= bx1 - shackle_t
            )

            # Keyhole: small circle + rectangle below
            kh_r  = int(size * 0.07)
            kh_cy = cy + int(size * 0.08)
            kh_dist = ((x - cx)**2 + (y - kh_cy)**2) ** 0.5
            kh_rect = (
                abs(x - cx) < int(size * 0.04) and
                y > kh_cy and
                y < kh_cy + int(size * 0.15)
            )
            in_keyhole = kh_dist < kh_r or kh_rect

            in_body = bx0 <= x <= bx1 and by0 <= y <= by1

            if in_body or in_shackle:
                if in_keyhole:
                    row.extend(bg)
                else:
                    row.extend(acc)
            else:
                row.extend(bg)

        pixels.append(bytes(row))

    def chunk(t, d):
        c = t + d
        return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)

    sig  = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
    raw  = b''.join(b'\x00' + r for r in pixels)
    idat = chunk(b'IDAT', zlib.compress(raw, 9))
    iend = chunk(b'IEND', b'')

    with open(path, 'wb') as f:
        f.write(sig + ihdr + idat + iend)
    print(f"  ✅ {path} ({size}×{size})")

if __name__ == '__main__':
    icons_dir = os.path.join(os.path.dirname(__file__), 'extension', 'icons')
    os.makedirs(icons_dir, exist_ok=True)
    print("Creating extension icons...")
    for s in [16, 48, 128]:
        make_png(s, os.path.join(icons_dir, f'icon{s}.png'))
    print("Done!")

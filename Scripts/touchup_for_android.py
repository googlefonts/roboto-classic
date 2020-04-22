import sys
from fontTools.ttLib import TTFont


YMIN = -555
YMAX = 2163


def main(font_path):
    font = TTFont(font_path, recalcBBoxes=False)

    # Force yMin and yMax
    font['head'].yMin = YMIN
    font['head'].yMax = YMAX

    # Enable Bold bits for Black styles
    if "Black" in font_path and "fvar" not in font:
        if "Italic" in font_path:
            font["OS/2"].fsSelection |= 32
        else:
            font["OS/2"].fsSelection ^= 64 | 32
        font["head"].macStyle |= 1
    font.save(font_path)


main(sys.argv[1])


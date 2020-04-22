import sys
from fontTools.ttLib import TTFont
from nototools import font_data


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

    # turn off round-to-grid flags in certain problem components
    # https://github.com/google/roboto/issues/153
    glyph_set = font.getGlyphSet()
    ellipsis = glyph_set['ellipsis']._glyph
    for component in ellipsis.components:
        component.flags &= ~(1 << 2)

    font_data.delete_from_cmap(font, [
        0x20E3, # COMBINING ENCLOSING KEYCAP
        0x2191, # UPWARDS ARROW
        0x2193, # DOWNWARDS ARROW
        ])
    font.save(font_path)


main(sys.argv[1])


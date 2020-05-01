from fontTools.ttLib import TTFont
import sys
import os


def set_vertical_metrics(ttfont):
    """Apply fixes needed for web fonts."""

    # set vertical metrics to old values
    ttfont['hhea'].ascent = 1900
    ttfont['hhea'].descent = -500

    ttfont['OS/2'].sTypoAscender = 1536
    ttfont['OS/2'].sTypoDescender = -512
    ttfont['OS/2'].sTypoLineGap = 102
    ttfont['OS/2'].usWinAscent = 1946
    ttfont['OS/2'].usWinDescent = 512


def update_nametable(ttfont):
    family_name = ttfont['name'].getName(16, 3, 1, 1033) or \
                  ttfont['name'].getName(1, 3, 1, 1033)
    style_name = ttfont['name'].getName(17, 3, 1, 1033) or \
                 ttfont['name'].getName(2, 3, 1, 1033)
    full_name = family_name.toUnicode() + " " + style_name.toUnicode()
    if full_name == "Roboto Regular":
        full_name = "Roboto"
    if full_name == "Roboto Condensed Regular":
        full_name = "Roboto Condensed"
    ttfont['name'].setName(full_name, 3,3,1,1033)
    ttfont['name'].setName(full_name, 4,3,1,1033)


def main(font_path):
    font = TTFont(font_path)
    filename = os.path.basename(font_path)
    if "Thin" in filename and "fvar" not in font:
        font['OS/2'].usWeightClass = 250
    # Disable Oblique bits
    if "BlackItalic" in filename and "fvar" not in font:
        font['OS/2'].fsSelection ^= 512
    set_vertical_metrics(font)
    update_nametable(font)
    font.save(font_path)


main(sys.argv[1])


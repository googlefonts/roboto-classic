from fontTools.ttLib import TTFont
import sys
import os


def set_vertical_metrics(ttfont):
    """Apply fixes needed for web fonts."""

    # set vertical metrics to old values
    ttfont['hhea'].ascent = 1900
    ttfont['hhea'].descent = -500

    ttfont['OS/2'].sTypoAscender = 1946
    ttfont['OS/2'].sTypoDescender = -512
    ttfont['OS/2'].sTypoLineGap = 0
    ttfont['OS/2'].usWinAscent = 1946
    ttfont['OS/2'].usWinDescent = 512

    # Enable fsSelection bit 7 (use typo metrics)
    ttfont["OS/2"].fsSelection |= (1 << 7)



def main(font_path):
    font = TTFont(font_path)
    filename = os.path.basename(font_path)
    if "Thin" in filename:
        font['OS/2'].usWeightClass = 250
    set_vertical_metrics(font)
    font.save(font_path)


main(sys.argv[1])


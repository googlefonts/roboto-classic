import sys
import os
from fontTools.ttLib import TTFont
from nototools import font_data
from scripts import *


def main(font_path):
    font = TTFont(font_path, recalcBBoxes=False)
    # Update vertical metrics to match v2.138
    update_attribs(
        font,
        **android_and_cros_vert_metrics
    )
    update_psname_and_fullname(font)
    update_font_version(font)
    disable_oblique_bits(font)
    # Enable Bold bits for Black fonts
    if "Black" in os.path.basename(font_path):
        font['head'].macStyle |= (1 << 0)
        font['OS/2'].fsSelection |= (1 << 5)
        font['OS/2'].fsSelection &= ~(1 << 6)
    font.save(font_path)


main(sys.argv[1])


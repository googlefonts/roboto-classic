import sys
from fontTools.ttLib import TTFont
from nototools import font_data
from scripts import *


def main(font_path):
    font = TTFont(font_path, recalcBBoxes=False)
    glyf = font["glyf"]
    # turn off round-to-grid flags in certain problem components
    # https://github.com/google/roboto/issues/153
    ellipsis = glyf['ellipsis']
    for component in ellipsis.components:
        component.flags &= ~(1 << 2)

    # Add first 32 control chars to font.
    # Has been specifically requested by Android team. They are
    # seeing tofus in Android's layout libs. This should be fixed in
    # the libs but it is easier for us to tweak the fonts.
    for table in font["cmap"].tables:
        for uni in range(32):
            if uni in table.cmap:
                continue
            table.cmap[uni] = "uni0002"

    font_data.delete_from_cmap(font, [
        0x20E3, # COMBINING ENCLOSING KEYCAP
        0x2191, # UPWARDS ARROW
        0x2193, # DOWNWARDS ARROW
        ])
    # Update vertical metrics to match v2.136
    update_attribs(
        font,
        **android_and_cros_vert_metrics
    )
    update_psname_and_fullname(font, include_year=True)
    update_font_version(font)
    font.save(font_path)


main(sys.argv[1])


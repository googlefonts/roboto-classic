import sys
from fontTools.ttLib import TTFont
from nototools import font_data
from scripts import *


def update_android_names(font):
    """v2.138 Android fonts do not use typographic records (nameIDs 16, 17).

    If a font contains typo records, replace nameIDs 1 and 2 with the typo
    records."""
    typo_family = font["name"].getName(16, 3, 1, 1033)
    typo_style = font["name"].getName(17, 3, 1, 1033)

    family = font["name"].getName(1, 3, 1, 1033)
    style = font["name"].getName(2, 3, 1, 1033)

    if typo_family:
        font["name"].setName(typo_family.toUnicode(), 1, 3, 1, 1033)
    if typo_style:
        font["name"].setName(typo_style.toUnicode(), 2, 3, 1, 1033)


def main(font_path):
    font = TTFont(font_path, recalcBBoxes=False)
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
    # Update vertical metrics to match v2.138
    update_attribs(
        font,
        **android_and_cros_vert_metrics
    )
    update_android_names(font)
    update_psname_and_fullname(font, include_year=True)
    update_font_version(font)
    disable_oblique_bits(font)
    font.save(font_path)


main(sys.argv[1])


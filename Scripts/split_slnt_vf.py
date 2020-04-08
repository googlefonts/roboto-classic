"""
...
"""
import argparse
import sys
import os
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import (
    instantiateVariableFont,
    sanityCheckVariableTables
)


def split_slnt(ttfont):
    """Use varlib instance to split a variable font if it contains a
    slnt or ital axis."""
    sanityCheckVariableTables(ttfont)

    axes = {a.axisTag: a for a in ttfont['fvar'].axes}
    ital_angle = axes['ital'].maxValue
    roman = instantiateVariableFont(ttfont, {"ital": 0})
    italic = instantiateVariableFont(ttfont, {"ital": ital_angle})

    _update_bits(italic)
    _update_nametable(italic)

    roman_filename = os.path.join(
        os.path.dirname(roman.reader.file.name),
        vf_filename(roman)
    )
    roman.save(roman_filename)
    italic_filename = os.path.join(
        os.path.dirname(italic.reader.file.name),
        vf_filename(italic)
    )
    italic.save(italic_filename)


def vf_filename(ttfont):
    axes = sorted([a.axisTag for a in ttfont['fvar'].axes])
    axes = ",".join(axes)
    family_name = ttfont['name'].getName(1, 3, 1, 1033)
    name = family_name.toUnicode()
    if "Italic" in ttfont['name'].getName(2, 3, 1, 1033).toUnicode():
        return f"{name}-Italic[{axes}].ttf"
    return f"{name}[{axes}].ttf"


def _update_bits(ttfont):
    """Update bits for instantiated italic font"""
    # OS/2: disable Regular bit and enable italic bit
    ttfont['OS/2'].fsSelection ^= (1 << 6) | 1
    # head: enable italic bit
    ttfont["head"].macStyle |= (1 << 1)

    ttfont["post"].italicAngle = -12 
    ttfont["hhea"].caretSlopeRun = 435
    ttfont["hhea"].caretSlopeRise = 2048


def _update_nametable(ttfont):
    nametable = ttfont['name']
    dflt_axes_loc = {a.axisTag: a.defaultValue for a in ttfont['fvar'].axes}
    dflt_nameid = None
    for instance in ttfont['fvar'].instances:
        if instance.coordinates == dflt_axes_loc:
            dflt_nameid = instance.subfamilyNameID
    if not dflt_nameid:
        raise ValueError("Cannot name font. Default axis locations are not represented by an instance.")
    dflt_name = nametable.getName(dflt_nameid, 3, 1, 1033).toUnicode()

    # Update subfamily name
    nametable.setName(dflt_name, 2, 3, 1, 1033)
    # Update unique font identifier
    version = "{:.3f}".format(ttfont['head'].fontRevision)
    vendor = ttfont['OS/2'].achVendID
    familyname = nametable.getName(1, 3, 1, 1033).toUnicode()
    unique_name = f"{version} {vendor} {familyname}-{dflt_name}"
    nametable.setName(unique_name, 3, 3, 1, 1033)
    # Update full font name
    full_font_name = f"{familyname} {dflt_name}"
    nametable.setName(full_font_name, 4, 3, 1, 1033)
    nametable.setName(full_font_name, 4, 1, 0, 0)
    # Postscript name
    postscript_name = f"{familyname}-{dflt_name}"
    nametable.setName(postscript_name, 6, 3, 1, 1033)
    nametable.setName(postscript_name, 6, 1, 0, 0)


def main():
    ttfont = TTFont(sys.argv[1])
    split_slnt(ttfont)


if __name__ == "__main__":
    main()


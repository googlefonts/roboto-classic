"""
...
"""
import argparse
import sys
import os
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables as ot
from fontTools.otlLib.builder import buildStatTable, _addName
from fontTools.varLib.instancer import (
    instantiateVariableFont,
    sanityCheckVariableTables
)


def split_slnt(ttfont, out_dir):
    """Use varlib instance to split a variable font if it contains a
    slnt or ital axis."""
    sanityCheckVariableTables(ttfont)

    axes = {a.axisTag: a for a in ttfont['fvar'].axes}
    ital_angle = axes['ital'].maxValue
    roman = instantiateVariableFont(ttfont, {"ital": 0})
    italic = instantiateVariableFont(ttfont, {"ital": ital_angle})

    _update_bits(italic)
    _update_nametable(italic)

    _update_fvar(roman)
    _update_fvar(italic)

    _update_roman_stat(roman)
    _update_italic_stat(italic)

    roman_filename = os.path.join(
        out_dir,
        vf_filename(roman)
    )
    roman.save(roman_filename)
    italic_filename = os.path.join(
        out_dir,
        vf_filename(italic)
    )
    italic.save(italic_filename)


def _update_fvar(ttfont):
    fvar = ttfont['fvar']
    nametable = ttfont['name']
    family_name = nametable.getName(16, 3, 1, 1033) or nametable.getName(1, 3, 1, 1033)
    family_name = family_name.toUnicode()
    font_style = "Italic" if "Italic" in nametable.getName(2, 3, 1, 1033).toUnicode() else "Roman"
    ps_family_name = f"{family_name.replace(' ', '')}{font_style}"
    nametable.setName(ps_family_name, 25, 3, 1, 1033)
    for instance in fvar.instances:
        instance_style = nametable.getName(instance.subfamilyNameID, 3, 1, 1033).toUnicode()
        instance_style = instance_style.replace("Italic", "").strip().replace(" ", "")
        if instance_style == "":
            instance_style = "Regular"
        ps_name = f"{ps_family_name}-{instance_style}"
        instance.postscriptNameID = _addName(nametable, ps_name, 256)


def _update_roman_stat(ttfont):
    stat = ttfont['STAT'].table

    record = ot.AxisValue()
    record.AxisIndex = 2
    record.Flags = 2
    record.ValueNameID = 296 # Roman
    record.LinkedValue = 1
    record.Value = 0
    record.Format = 3

    stat.AxisValueArray.AxisValue[-1] = record


def _update_italic_stat(ttfont):
    stat = ttfont['STAT'].table

    record = ot.AxisValue()
    record.AxisIndex = 2
    record.Flags = 0
    record.ValueNameID = 258 # Italic
    record.Value = 1.0
    record.Format = 1

    stat.AxisValueArray.AxisValue[-1] = record


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
    familyname = nametable.getName(1, 3, 1, 1033).toUnicode()

    # Update subfamily name
    nametable.setName(dflt_name, 2, 3, 1, 1033)
    # Update full font name and uniqueID
    full_font_name = f"{familyname} {dflt_name}"
    nametable.setName(full_font_name, 3, 3, 1, 1033)
    nametable.setName(full_font_name, 4, 3, 1, 1033)
    nametable.setName(full_font_name, 4, 1, 0, 0)
    # Postscript name
    postscript_name = f"{familyname}-{dflt_name}"
    nametable.setName(postscript_name, 6, 3, 1, 1033)
    nametable.setName(postscript_name, 6, 1, 0, 0)


def main():
    ttfont = TTFont(sys.argv[1])
    split_slnt(ttfont, sys.argv[2])


if __name__ == "__main__":
    main()


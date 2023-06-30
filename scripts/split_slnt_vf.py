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
    roman = instantiateVariableFont(ttfont, {"ital": 0}, updateFontNames=True)
    italic = instantiateVariableFont(ttfont, {"ital": ital_angle}, updateFontNames=True)

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


def main():
    ttfont = TTFont(sys.argv[1])
    split_slnt(ttfont, sys.argv[2])


if __name__ == "__main__":
    main()


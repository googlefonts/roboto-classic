from fontbakery.callable import check
from fontbakery.callable import condition
from fontbakery.checkrunner import Section, PASS, FAIL, WARN
from fontbakery.fonts_profile import profile_factory
from tests.test_general import (
    font_family,
    font_style,
    font_features,
    com_roboto_fonts_check_italic_angle,
    com_roboto_fonts_check_fs_type,
    com_roboto_fonts_check_vendorid,
    com_roboto_fonts_check_digit_widths,
    com_roboto_fonts_check_features,
    com_roboto_fonts_check_charset_coverage,
    exclude_glyphs,
)
from fontbakery.profiles.shared_conditions import is_italic


@condition
def include_glyphs():
    # Ensure superior and inferior figures are included
    # https://github.com/googlefonts/roboto-classic/issues/97
    return frozenset([
        0x2070,
        0x2074,
        0x2075,
        0x2076,
        0x2077,
        0x2078,
        0x2079,
        0x2080,
        0x2081,
        0x2082,
        0x2083,
        0x2084,
        0x2085,
        0x2086,
        0x2087,
        0x2088,
        0x2089,
    ])

@condition
def include_features():
    return set([
        'c2sc', 'ccmp', 'cpsp', 'dlig', 'dnom', 'frac', 'kern', 'liga', 'lnum',
        'locl', 'numr', 'onum', 'pnum', 'smcp', 'ss01', 'ss02', 'ss03', 'ss04',
        'ss05', 'ss06', 'ss07', 'tnum', 'sups', 'subs'])

profile = profile_factory(default_section=Section("Roboto web v3"))

ROBOTO_PROFILE_CHECKS = [
    "com.roboto.fonts/check/vertical_metrics",
    "com.roboto.fonts/check/oblique_bits_not_set",
    "com.roboto.fonts/check/unique_id",
    "com.roboto.fonts/check/hinting",
    "com.roboto.fonts/check/italic_angle",
    "com.roboto.fonts/check/fs_type",
    "com.roboto.fonts/check/vendorid",
    "com.roboto.fonts/check/digit_widths",
    "com.roboto.fonts/check/features",
    "com.roboto.fonts/check/charset_coverage",
]


@check(
    id="com.roboto.fonts/check/vertical_metrics",
)
def com_roboto_fonts_check_vertical_metrics(ttFont):
    """Check vertical metrics are correct"""
    failed = []
    expected = {
        # android requires this, and web fonts expect this
        ("head", "yMin"): -555,
        ("head", "yMax"): 2163,
        # test hhea ascent, descent, and lineGap to be equal to Roboto v1 values
        ("hhea", "descent"): -500,
        ("hhea", "ascent"): 1900,
        ("hhea", "lineGap"): 0,
        # test OS/2 vertical metrics to be equal to old OS/2 win values
        # since fsSelection bit 7 is now enabled
        ("OS/2", "sTypoDescender"): -512,
        ("OS/2", "sTypoAscender"): 1536,
        ("OS/2", "sTypoLineGap"): 102,
        ("OS/2", "usWinDescent"): 512,
        ("OS/2", "usWinAscent"): 1946,
    }
    for (table, k), v in expected.items():
        font_val = getattr(ttFont[table], k)
        if font_val != v:
            failed.append((table, k, v, font_val))
    if not failed:
        yield PASS, "Fonts have correct vertical metrics"
    else:
        msg = "\n".join(
            [
                f"- {tbl}.{k} is {font_val} it should be {v}"
                for tbl, k, v, font_val in failed
            ]
        )
        yield FAIL, f"Fonts have incorrect vertical metrics:\n{msg}"


@check(
    id="com.roboto.fonts/check/oblique_bits_not_set",
)
def com_roboto_fonts_check_oblique_bits_not_set(ttFont):
    """Check oblique bits are not set in fonts"""
    if ttFont['OS/2'].fsSelection & (1 << 9) != 0:
        yield FAIL, "fsSelection bit 9 (Oblique) must not be enabled"
    else:
        yield PASS, "fsSelection bit 9 is disabled"


@check(
    id="com.roboto.fonts/check/unique_id",
)
def com_roboto_fonts_check_unique_id(ttFont):
    """Check font unique id is correct"""
    family_name = font_family(ttFont)
    style = font_style(ttFont)
    if style != "Regular":
        expected = f"{family_name} {style}"
    else:
        expected = f"{family_name}"
    font_unique_id = ttFont['name'].getName(3, 3, 1, 1033).toUnicode()
    if font_unique_id == expected:
        yield PASS, "Unique ID is correct"
    else:
        yield FAIL, f"Unique ID, '{font_unique_id}' is incorrect. It should be '{expected}'"



@check(
    id="com.roboto.fonts/check/hinting",
)
def com_roboto_fonts_check_hinting(ttFont):
    """Check glyphs have hinting"""
    missing_hints = []
    # we can ignore these according to Mike D
    # https://github.com/TypeNetwork/Roboto/issues/70#issuecomment-641221200
    ignore = ['.notdef', 'uni0488', 'uni0489', 'uniFFFC', 'uniFFFD']
    for glyph_name in ttFont.getGlyphOrder():
        glyph = ttFont['glyf'][glyph_name]
        if glyph.numberOfContours <= 0:
            continue
        if len(glyph.program.bytecode) <= 0 and glyph_name not in ignore:
            missing_hints.append(glyph_name)
    if missing_hints:
        yield FAIL, f"Following glyphs are missing hinting {missing_hints}"
    else:
        yield PASS, "All glyphs are hinted"


profile.auto_register(globals())
profile.test_expected_checks(ROBOTO_PROFILE_CHECKS, exclusive=True)

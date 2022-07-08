from fontbakery.callable import check
from fontbakery.callable import condition
from fontbakery.checkrunner import Section, PASS, FAIL, WARN
from fontbakery.fonts_profile import profile_factory
from tests.test_general import (
    is_italic,
    com_roboto_fonts_check_italic_angle,
    com_roboto_fonts_check_fs_type,
    com_roboto_fonts_check_vendorid,
    com_roboto_fonts_check_digit_widths,
    com_roboto_fonts_check_charset_coverage,
)

profile = profile_factory(default_section=Section("Roboto android v3"))

exclude_glyphs = frozenset([0x00A0])

ROBOTO_PROFILE_CHECKS = [
    "com.roboto.fonts/check/vertical_metrics",
    "com.roboto.fonts/check/italic_angle",
    "com.roboto.fonts/check/fs_type",
    "com.roboto.fonts/check/vendorid",
    "com.roboto.fonts/check/digit_widths",
    "com.roboto.fonts/check/glyph_dont_round_to_grid",
    "com.roboto.fonts/check/charset_coverage",
]


@condition
def include_glyphs():
    return frozenset([
        0x2117,  # SOUND RECORDING COPYRIGHT
        0xEE01, 0xEE02, 0xF6C3] +
        list(range(0x0000, 0x0020)) # First 32 control characters
    )  # legacy PUA


@condition
def exclude_glyphs():
    return frozenset([
        0x20E3,  # COMBINING ENCLOSING KEYCAP
        0x2191,  # UPWARDS ARROW
        0x2193,  # DOWNWARDS ARROW
        0x2072, 0x2073, 0x208F] +  # unassigned characters
        list(range(0xE000, 0xF8FF + 1)) + list(range(0xF0000, 0x10FFFF + 1))  # other PUA
        ) - include_glyphs()  # don't exclude legacy PUA


@check(
    id="com.roboto.fonts/check/glyph_dont_round_to_grid",
)
def com_roboto_fonts_check_glyph_dont_round_to_grid(ttFont):
    """Test certain glyphs don't round to grid"""
    failed = False
    glyphset = ttFont.getGlyphSet()
    for name in ["ellipsis"]:
        glyph = glyphset[name]._glyph
        for component in glyph.components:
            if component.flags & (1 << 2):
                failed = True
                yield FAIL, f"Round to grid flag must be disabled for '{name}' components"
    if not failed:
        yield PASS, "Glyphs do not have round to grid enabled"


# test names


@check(
    id="com.roboto.fonts/check/vertical_metrics",
)
def com_roboto_fonts_check_vertical_metrics(ttFont):
    """Check vertical metrics are correct"""
    failed = []
    expected = {
        # Android values come from v2.136 android fonts
        # https://github.com/googlefonts/roboto/releases/tag/v2.136
        ("head", "yMin"): -555,
        ("head", "yMax"): 2163,
        ("hhea", "descent"): -500,
        ("hhea", "ascent"): 1900,
        ("hhea", "lineGap"): 0,
        ("OS/2", "sTypoDescender"): -555,
        ("OS/2", "sTypoAscender"): 2146,
        ("OS/2", "sTypoLineGap"): 0,
        ("OS/2", "usWinDescent"): 555,
        ("OS/2", "usWinAscent"): 2146,
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


# ligatures

profile.auto_register(globals())
profile.test_expected_checks(ROBOTO_PROFILE_CHECKS, exclusive=True)

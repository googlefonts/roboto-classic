from fontbakery.callable import check
from fontbakery.callable import condition
from fontbakery.checkrunner import Section, PASS, FAIL, WARN
from fontbakery.fonts_profile import profile_factory
from fontbakery.profiles.universal import UNIVERSAL_PROFILE_CHECKS

# profile_imports = ('fontbakery.profiles.universal',)
profile = profile_factory(default_section=Section("Roboto v3"))

ROBOTO_PROFILE_CHECKS = [
    "com.roboto.fonts/check/vertical_metrics",
    "com.roboto.fonts/check/italic_angle",
    "com.roboto.fonts/check/meta_info"
]


@condition
def is_italic(ttFont):
    return True if "Italic" in ttFont.reader.file.name else False


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
        ("OS/2", "sTypoAscender"): 1946,
        ("OS/2", "sTypoLineGap"): 0,
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
    id="com.roboto.fonts/check/italic_angle",
    conditions = ["is_italic"]
)
def com_roboto_fonts_check_italic_angle(ttFont):
    """Check vertical metrics are correct"""
    failed = False
    if ttFont['post'].italicAngle != -12:
        yield FAIL, "post.italicAngle must be set to -12"
    else:
        yield PASS, "post.italicAngle is set correctly"

    if ttFont["OS/2"].achVendID != "GOOG":
        yield FAIL, "OS/2.achVendID must be set to 'GOOG'"
    else:
        yield PASS, "OS/2.achVendID is set corrrectly"


@check(
    id="com.roboto.fonts/check/meta_info",
)
def com_roboto_fonts_check_meta_info(ttFont):
    """Check metadata is correct"""
    failed = False
    if ttFont['OS/2'].fsType != 0:
        yield FAIL, "OS/2.fsType must be 0"
    else:
        yield PASS, "OS/2.fsType is set correctly"


profile.auto_register(globals())
profile.test_expected_checks(ROBOTO_PROFILE_CHECKS, exclusive=True)

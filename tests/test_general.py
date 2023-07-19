from fontbakery.callable import check
from fontbakery.callable import condition
from fontbakery.checkrunner import Section, PASS, FAIL, WARN
from fontbakery.fonts_profile import profile_factory
from fontbakery.profiles.universal import UNIVERSAL_PROFILE_CHECKS
from fontbakery.profiles.googlefonts_conditions import (
    style,
    expected_style,
    familyname_with_spaces,
    familyname,
)
from fontbakery.profiles.googlefonts import (
    com_google_fonts_check_usweightclass,
    com_google_fonts_check_fsselection,
    com_google_fonts_check_name_familyname,
)
from nototools.unittests import layout


# These checks fail in V2. If we try and make these checks pass, we
# will cause regressions. This isn't acceptable for a family which is
# requested 40 billion times a week.
REMOVE_CHECKS = [
    "com.google.fonts/check/required_tables",
    "com.google.fonts/check/family/win_ascent_and_descent",
    "com.google.fonts/check/os2_metrics_match_hhea",
    "com.google.fonts/check/ftxvalidator_is_available",
    "com.google.fonts/check/dsig",
    "com.google.fonts/check/fontbakery_version",
    "com.google.fonts/check/outline_semi_vertical",
    "com.google.fonts/check/outline_jaggy_segments",
    "com.google.fonts/check/outline_colinear_vectors",
    "com.google.fonts/check/outline_short_segments",
    "com.google.fonts/check/outline_alignment_miss",
    "com.adobe.fonts/check/varfont/valid_default_instance_nameids",
]


def filter_checks(_, check_id, __):
    if check_id in REMOVE_CHECKS:
        return False
    return True


GOOGLEFONTS_PROFILE_CHECKS = [
    'com.google.fonts/check/usweightclass',
    'com.google.fonts/check/fsselection',
    'com.google.fonts/check/name/familyname',
]

ROBOTO_GENERAL_CHECKS = [c for c in UNIVERSAL_PROFILE_CHECKS + GOOGLEFONTS_PROFILE_CHECKS
                         if c not in REMOVE_CHECKS]

ROBOTO_GENERAL_CHECKS += [
    "com.roboto.fonts/check/italic_angle",
    "com.roboto.fonts/check/fs_type",
    "com.roboto.fonts/check/vendorid",
    "com.roboto.fonts/check/charset_coverage",
    "com.roboto.fonts/check/digit_widths",
    "com.roboto.fonts/check/numr_mapped_to_supr",
    "com.roboto.fonts/check/name_copyright",
    "com.roboto.fonts/check/name_unique_id",
    "com.roboto.fonts/check/vertical_metrics",
    "com.roboto.fonts/check/cmap4",
    "com.roboto.fonts/check/features",
]

profile_imports = ('fontbakery.profiles.universal',)
profile = profile_factory(default_section=Section("Roboto v3 general"))


# Checks ported from https://github.com/googlefonts/roboto/blob/master/scripts/run_general_tests.py


@condition
def is_vf(ttFont):
    return True if "fvar" in ttFont else False


@condition
def font_features(ttFont):
    if "GSUB" not in ttFont:
        return []
    gsub = set(f.FeatureTag for f in ttFont["GSUB"].table.FeatureList.FeatureRecord)
    if "GPOS" not in ttFont:
        return gsub
    gpos = set(f.FeatureTag for f in ttFont["GPOS"].table.FeatureList.FeatureRecord)
    return gsub | gpos


@condition
def include_features():
    return frozenset(
        [
            'frac',
            'subs',
            'salt',
            'numr',
            'sups',
            'unic',
            'ccmp',
            'c2sc',
            'smcp',
            'dnom',
            'dlig',
            'onum',
            'lnum',
            'tnum',
            'ss06',
            'ss07',
            'ss02',
            'ss01',
            'ss04',
            'liga',
            'locl',
            'ss05',
            'pnum',
            'ss03'
        ]
    )


def font_style(ttFont):
    subfamily_name = ttFont['name'].getName(2, 3, 1, 1033)
    typo_subfamily_name = ttFont['name'].getName(17, 3, 1, 1033)
    if typo_subfamily_name:
        return typo_subfamily_name.toUnicode()
    return subfamily_name.toUnicode()


def font_family(ttFont):
    family_name = ttFont['name'].getName(1, 3, 1, 1033)
    typo_family_name = ttFont['name'].getName(16, 3, 1, 1033)
    if typo_family_name:
        return typo_family_name.toUnicode()
    return family_name.toUnicode()


@check(
    id="com.roboto.fonts/check/italic_angle",
    conditions = ["is_italic"]
)
def com_roboto_fonts_check_italic_angle(ttFont):
    """Check italic fonts have correct italic angle"""
    failed = False
    if ttFont['post'].italicAngle != -12:
        yield FAIL, "post.italicAngle must be set to -12"
    else:
        yield PASS, "post.italicAngle is set correctly"


@check(
    id="com.roboto.fonts/check/fs_type",
)
def com_roboto_fonts_check_fs_type(ttFont):
    """Check metadata is correct"""
    failed = False
    if ttFont['OS/2'].fsType != 0:
        yield FAIL, "OS/2.fsType must be 0"
    else:
        yield PASS, "OS/2.fsType is set correctly"


@check(
    id="com.roboto.fonts/check/vendorid",
)
def com_roboto_fonts_check_vendorid(ttFont):
    """Check vendorID is correct"""
    if ttFont["OS/2"].achVendID != "GOOG":
        yield FAIL, "OS/2.achVendID must be set to 'GOOG'"
    else:
        yield PASS, "OS/2.achVendID is set corrrectly"


@check(
    id="com.roboto.fonts/check/name_copyright",
)
def com_roboto_fonts_check_copyright(ttFont):
    """Check font copyright is correct"""
    expected_copyright = "Copyright 2011 Google Inc. All Rights Reserved."
    copyright_record = ttFont['name'].getName(0, 3, 1, 1033).toUnicode()
    if copyright_record == expected_copyright:
        yield PASS, "Copyright is correct"
    else:
        yield FAIL, f"Copyright is incorrect. It should be {expected_copyright}"


@check(
    id="com.roboto.fonts/check/name_unique_id",
)
def com_roboto_fonts_check_name_unique_id(ttFont):
    """Check font unique id is correct"""
    family_name = font_family(ttFont)
    style = font_style(ttFont)
    expected = f"Google:{family_name} {style}:2016"
    font_unique_id = ttFont['name'].getName(3, 3, 1, 1033).toUnicode()
    if font_unique_id == expected:
        yield PASS, "Unique ID is correct"
    else:
        yield FAIL, f"Unique ID, '{font_unique_id}' is incorrect. It should be '{expected}'"



@check(
    id="com.roboto.fonts/check/digit_widths",
)
def com_roboto_fonts_check_digit_widths(ttFont):
    """Check that all digits have the same width"""
    widths = set()
    for glyph_name in ["zero", "one", "two", "three","four", "five", "six", "seven", "eight", "nine"]:
        widths.add(ttFont['hmtx'][glyph_name][0])
    if len(widths) != 1:
        yield FAIL, "Numerals 0-9 do not have the same width"
    else:
        yield PASS, "Numerals 0-9 have the same width"


@check(
    id="com.roboto.fonts/check/numr_mapped_to_supr",
)
def com_roboto_fonts_check_numr_mapped_to_supr(ttFont):
    """Check that 'numr' features maps digits to Unicode superscripts."""
    ascii_digits = '0123456789'
    superscript_digits = u'⁰¹²³⁴⁵⁶⁷⁸⁹'

    numr_glyphs = layout.get_advances(
        ascii_digits, ttFont.reader.file.name, '--features=numr')
    superscript_glyphs = layout.get_advances(
        superscript_digits, ttFont.reader.file.name)
    if superscript_glyphs == numr_glyphs:
        yield PASS, "'numr' feature mapped to unicode superscript glyphs"
    else:
        yield FAIL, "'numr' feature is not mapped to unicode superscript glyphs"


@condition
def include_glyphs():
    return frozenset([
        0x2117,  # SOUND RECORDING COPYRIGHT
        0xEE01, 0xEE02, 0xF6C3, # legacy PUA
        # superior and inferior glyphs
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
def exclude_glyphs():
    return frozenset([
        0x2072, 0x2073, 0x208F] +  # unassigned characters
        list(range(0xE000, 0xF8FF + 1)) + list(range(0xF0000, 0x10FFFF + 1))  # other PUA
    ) - include_glyphs()  # don't exclude legacy PUA


@check(
    id="com.roboto.fonts/check/charset_coverage",
    conditions = ["include_glyphs", "exclude_glyphs"]
)
def com_roboto_fonts_check_charset_coverage(ttFont, include_glyphs, exclude_glyphs):
    """Check to make sure certain unicode encoded glyphs are included and excluded"""
    font_unicodes = set(ttFont.getBestCmap().keys())

    to_include = include_glyphs - font_unicodes
    if to_include != set():
        yield FAIL, f"Font must include the following codepoints {list(map(hex, to_include))}"
    else:
        yield PASS, "Font includes correct encoded glyphs"

    to_exclude = exclude_glyphs - font_unicodes
    if to_exclude != exclude_glyphs:
        yield FAIL, f"Font must exclude the following codepoints {list(map(hex, to_exclude))}"
    else:
        yield PASS, "Font excludes correct encoded glyphs"

# TODO TestLigatures

# TODO TestFeatures

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


@check(
    id="com.roboto.fonts/check/cmap4",
)
def com_roboto_fonts_check_cmap4(ttFont):
    """Check fonts have cmap format 4"""
    cmap_table = ttFont['cmap'].getcmap(3, 1)
    if cmap_table and cmap_table.format == 4:
        yield PASS, "Font contains a MS Unicode BMP encoded cmap"
    else:
        yield FAIL, "Font does not contain a MS Unicode BMP encoded cmap"


@check(
    id="com.roboto.fonts/check/features",
)
def com_roboto_fonts_check_features(font_features, include_features):
    """Check font has correct features.
    https://github.com/googlefonts/roboto-classic/issues/97"""
    missing = include_features - font_features
    if missing:
        yield FAIL, f"Font is missing features {missing}"
    else:
        yield PASS, "Font has correct features"


profile.auto_register(globals(), filter_func=filter_checks)
profile.test_expected_checks(ROBOTO_GENERAL_CHECKS, exclusive=False)


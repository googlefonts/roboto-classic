# Roboto VF

Source UFOs were build from roboto v2.136 after fixing a couple glyphs for compatibility:

- Roboto-Bold.ufo/glyphs/bhook.cn.glif
- Roboto-Bold.ufo/glyphs/dhook.cn.glif
- Roboto-Bold.ufo/glyphs/eshcurl.glif
- Roboto-Bold.ufo/glyphs/ghook.cn.glif
- Roboto-Bold.ufo/glyphs/phook.cn.glif
- Roboto-Bold.ufo/glyphs/qhook.cn.glif
- Roboto-Bold.ufo/glyphs/uni2185.cn.glif
- Roboto-Bold.ufo/glyphs/uniA758_.cn.glif
- Roboto-Bold.ufo/glyphs/uniA797_.cn.glif
- Roboto-Bold.ufo/glyphs/uniAB36__.cn.glif
- Roboto-Bold.ufo/glyphs/uniAB36__.glif
- Roboto-Regular.ufo/glyphs/bhook.cn.glif
- Roboto-Regular.ufo/glyphs/dhook.cn.glif
- Roboto-Regular.ufo/glyphs/ghook.cn.glif
- Roboto-Regular.ufo/glyphs/hornnosp.glif
- Roboto-Regular.ufo/glyphs/phook.cn.glif
- Roboto-Regular.ufo/glyphs/qhook.cn.glif
- Roboto-Regular.ufo/glyphs/uni2185.cn.glif
- Roboto-Regular.ufo/glyphs/uniA758_.cn.glif
- Roboto-Regular.ufo/glyphs/uniA797_.cn.glif
- Roboto-Regular.ufo/glyphs/uniAB36__.cn.glif
- Roboto-Regular.ufo/glyphs/uniAB36__.glif
- Roboto-Thin.ufo/glyphs/bhook.cn.glif
- Roboto-Thin.ufo/glyphs/dhook.cn.glif
- Roboto-Thin.ufo/glyphs/ghook.cn.glif
- Roboto-Thin.ufo/glyphs/phook.cn.glif
- Roboto-Thin.ufo/glyphs/qhook.cn.glif
- Roboto-Thin.ufo/glyphs/uni2185.cn.glif
- Roboto-Thin.ufo/glyphs/uniA758_.cn.glif
- Roboto-Thin.ufo/glyphs/uniA797_.cn.glif
- Roboto-Thin.ufo/glyphs/uniAB36__.cn.glif
- Roboto-Thin.ufo/glyphs/uniAB36__.glif

Then the build script was edited to preserve glyph overlap.

- scripts/build-v2.py
- scripts/lib/fontbuild/Build.py

The [master_ufo](master_ufo/) folder contains the new UFOs.

The [fonts](fonts/) folder contains the variation font.

**Roboto-min-VF.ttf** has deltas for min, default and max

**Roboto-VF.ttf** has deltas min, default, max and also intermediate instances

Both fonts have all named instances:

- Thin- Thin Italic
- Light- Light Italic- Regular
- Italic
- Medium- Medium Italic
- Bold- Bold Italic
- Black- Black Italic
- Condensed Light- Condensed Light Italic
- Condensed Regular- Condensed Italic
- Condensed Bold- Condensed Bold Italic
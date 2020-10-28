import defcon
from glob import glob
import os
import shutil


srcs = {os.path.basename(f): f for f in glob("sources/*.ufo")}
new_paths = {os.path.basename(f): f for f in glob("sources/master_ufo/*.ufo")}

missing = set(srcs.keys()) ^ set(new_paths.keys())
if missing:
    print('missing', missing)
    import sys
    sys.exit()

for glyph in ["uni0472.glif", "uni0473.glif","theta.glif", "uni04E_8.smcp.glif"]:
    for k in new_paths:
        new_path = os.path.join(new_paths[k], "glyphs", glyph)
        cur_path = os.path.join(srcs[k], "glyphs", glyph)
        shutil.move(new_path, cur_path)

        print(new_path)
        print(cur_path)
        print()


import defcon
from glob import glob


sources = glob('/Users/marcfoley/Type/upstream_families/Roboto/sources/*.ufo')

for source in sources:
    font = defcon.Font(source)
    font.info.trademark = "Roboto is a trademark of Google."
    print(f"Saving {source}")
    font.save(source)


import defcon
from glob import glob

VERSION_MAJOR = 3
VERSION_MINOR = 3

sources = glob("sources/*.ufo")

for path in sources:
    print(f"Updating {path}")
    font = defcon.Font(path)
    font.info.versionMajor = VERSION_MAJOR
    font.info.versionMinor = VERSION_MINOR
    font.save(path)

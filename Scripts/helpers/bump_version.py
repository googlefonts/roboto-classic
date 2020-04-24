import defcon
from glob import glob

VERSION_MAJOR = 3
VERSION_MINOR = 0

sources = glob("sources/*.ufo")

for path in sources:
    print(f"Updating {path}")
    font = defcon.Font(path)
    font.info.versionMajor = VERSION_MAJOR
    font.info.versionMinor = VERSION_MINOR
    font.save(path)

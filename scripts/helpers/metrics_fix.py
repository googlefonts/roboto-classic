import defcon
from glob import glob


sources = glob('/Users/marcfoley/Type/upstream_families/Roboto/sources/*.ufo')

for source in sources:
    font = defcon.Font(source)
    if font.info.openTypeOS2Selection == [7, 7]:
        font.info.openTypeOS2Selection = [7]
    elif font.info.openTypeOS2Selection == [9, 7, 7]:
        font.info.openTypeOS2Selection = [9, 7]

    # fix vertical metrics
    font.info.openTypeOS2TypoAscender = 2146
    font.info.openTypeOS2TypoDescender = -555
    font.info.openTypeOS2TypoLineGap = 0
    font.info.openTypeOS2WinAscent = 2146
    font.info.openTypeOS2WinDescent = 555
    print(f"Saving {source}")
    font.save(source)


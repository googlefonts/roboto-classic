for font in AllFonts():
    print(font.info.openTypeOS2TypoLineGap)
    print(font.info.openTypeOS2WinAscent)
    print(font.info.openTypeOS2WinDescent)
    print(font.info.openTypeHheaLineGap)
    
    font.info.openTypeHheaAscender = 1900
    font.info.openTypeHheaDescender = -500
    font.info.openTypeHheaLineGap = 0
    
    font.info.openTypeOS2TypoLineGap = 102
    font.info.openTypeOS2WinAscent = 1946
    font.info.openTypeOS2WinDescent = 512
    print(font.info.openTypeOS2TypoLineGap)
    print(font.info.openTypeOS2WinAscent)
    print(font.info.openTypeOS2WinDescent)
    print(font.info.openTypeHheaLineGap)
    font.save()
    
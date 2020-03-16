
#font = CurrentFont()

names = ["uni0313", "uni0315", "uni1DCE", "uni1DE0", "uni1DEE", "emdash", "uni2094", "uni2DEC", "uni2E0D", "uni2E15", "uni2E1D", "uni2E32", "uni2E3A", "uni2E3B", "uniA780", "uniAB51", "commaaboverightcomb"]

for font in AllFonts():
    for glyph in font:
        #print (unicodes)
        if glyph.name in names:
            glyph.selected = True 
            print("selected " + glyph.name)
            glyph.decompose()
    font.save()
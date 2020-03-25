font = CurrentFont()

#print (font.glyphOrder)

index = 0

fullGlyphOrder = []

for glyph in font.glyphOrder:
    
    my_list = [ str(index) , glyph , str( font[glyph].unicode ) ]
    fullGlyphOrder.append( my_list )
    #print( str(index) + "," + glyph + "," + str( font[glyph].unicode ) )
    index+=1

print (fullGlyphOrder)

#print ( hex(58) )
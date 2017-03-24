font = CurrentFont()
    
unichars = u""
for glyph in font.glyphOrder:

    unis = font[glyph].unicodes
    
    if unis:
        
        if len(unis) == 1:
            
            uni = unis[0]
            
            try:
                unichars += unichr(uni)
            except ValueError:
                pass #print hex(uni)


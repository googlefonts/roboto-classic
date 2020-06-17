for f in AllFonts():

    #f = CurrentFont()

    # copy space-separated glyph names here
    glyphsToRemove = "Agrave Aacute Acircumflex Atilde Adieresis Aring Ccedilla Egrave Eacute Ecircumflex Edieresis Igrave Iacute Icircumflex Idieresis Ntilde Ograve Oacute Ocircumflex Otilde Odieresis Ugrave Uacute Ucircumflex Udieresis Yacute agrave aacute acircumflex atilde adieresis aring ccedilla egrave eacute ecircumflex edieresis igrave iacute icircumflex idieresis ntilde ograve oacute ocircumflex otilde odieresis ugrave uacute ucircumflex udieresis yacute ydieresis Amacron amacron Abreve abreve Cacute cacute Ccircumflex ccircumflex uni010A Cdotaccent uni010B cdotaccent Ccaron ccaron Dcaron Emacron emacron Ebreve ebreve Edotaccent edotaccent Ecaron ecaron Gcircumflex gcircumflex Gbreve gbreve uni0120 Gdotaccent uni0121 gdotaccent Gcommaaccent gcommaaccent Hcircumflex hcircumflex Itilde itilde Imacron imacron Ibreve ibreve Idotaccent Jcircumflex jcircumflex Kcommaaccent kcommaaccent Lacute lacute Lcommaaccent lcommaaccent Nacute nacute Ncommaaccent ncommaaccent Ncaron ncaron Omacron omacron Obreve obreve Ohungarumlaut ohungarumlaut Racute racute Rcommaaccent rcommaaccent Rcaron rcaron Sacute sacute Scircumflex scircumflex Scedilla scedilla Scaron scaron uni0162 Tcedilla uni0163 tcedilla Tcaron Utilde utilde Umacron umacron Ubreve ubreve Uring uring Uhungarumlaut uhungarumlaut Wcircumflex wcircumflex Ycircumflex ycircumflex Ydieresis Zacute zacute Zdotaccent zdotaccent Zcaron zcaron Gcaron gcaron AEacute aeacute Oslashacute oslashacute uni0218 Scommaaccent uni0219 scommaaccent uni021A Tcommaaccent uni021B tcommaaccent Ymacron uni0232 ymacron uni0233 Wgrave wgrave Wacute wacute Wdieresis wdieresis Ygrave ygrave"
#    glyphsToRemove = "Cacute cacute"

    # clean up the rest of the data
    for glyphToRemove in glyphsToRemove.split(" "):
        
        # # remove from keys
        # if glyphToRemove in f.keys():
        #     del f[glyphToRemove]
            

        # # remove from glyphOrder 
        #  for glyphName in f.glyphOrder:
        #      if glyphName == glyphToRemove:
        #          del f.glyphOrder[glyphName]

        # GROUPS ------------------------------------------------------------

        # iterate over all groups in the font
        for groupName in f.groups.keys():

            # get the group
            group = f.groups[groupName]
            groupList = list(f.groups[groupName])

            # if glyph is in the group, remove it
            if glyphToRemove in group:
                print('removing %s from group %s...' % (glyphToRemove, groupName))
                groupList.remove(glyphToRemove)
                f.groups[groupName] = tuple(groupList)

        # KERNING -----------------------------------------------------------

        # iterate over all kerning pairs in the font
        for kerningPair in f.kerning.keys():

            # if glyph is in the kerning pair, remove it
            if glyphToRemove in kerningPair:
                print('removing kerning pair (%s, %s)...' % kerningPair)
                del f.kerning[kerningPair]

        # COMPONENTS --------------------------------------------------------

        # iterate over all glyphs in the font
        for glyph in f:

            # skip glyphs which don’t have components
            if not glyph.components:
                continue

            # iterate over all components in glyph
            for component in glyph.components:

                # if the base glyph is the glyph to be removed
                if component.baseGlyph == glyphToRemove:
                    # delete the component
                    glyph.removeComponent(component)

    f.save()
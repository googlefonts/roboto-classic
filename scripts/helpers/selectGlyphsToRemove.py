
f=CurrentFont()

glyphsToRemove = "Agrave Aacute Acircumflex Atilde Adieresis Aring Ccedilla Egrave Eacute Ecircumflex Edieresis Igrave Iacute Icircumflex Idieresis Ntilde Ograve Oacute Ocircumflex Otilde Odieresis Ugrave Uacute Ucircumflex Udieresis Yacute agrave aacute acircumflex atilde adieresis aring ccedilla egrave eacute ecircumflex edieresis igrave iacute icircumflex idieresis ntilde ograve oacute ocircumflex otilde odieresis ugrave uacute ucircumflex udieresis yacute ydieresis Amacron amacron Abreve abreve Cacute cacute Ccircumflex ccircumflex uni010A uni010B Ccaron ccaron Dcaron Emacron emacron Ebreve ebreve Edotaccent edotaccent Ecaron ecaron Gcircumflex gcircumflex Gbreve gbreve uni0120 uni0121 Gcommaaccent gcommaaccent Hcircumflex hcircumflex Itilde itilde Imacron imacron Ibreve ibreve Idotaccent Jcircumflex jcircumflex Kcommaaccent kcommaaccent Lacute lacute Lcommaaccent lcommaaccent Nacute nacute Ncommaaccent ncommaaccent Ncaron ncaron Omacron omacron Obreve obreve Ohungarumlaut ohungarumlaut Racute racute Rcommaaccent rcommaaccent Rcaron rcaron Sacute sacute Scircumflex scircumflex Scedilla scedilla Scaron scaron uni0162 uni0163 Tcaron Utilde utilde Umacron umacron Ubreve ubreve Uring uring Uhungarumlaut uhungarumlaut Wcircumflex wcircumflex Ycircumflex ycircumflex Ydieresis Zacute zacute Zdotaccent zdotaccent Zcaron zcaron Gcaron gcaron AEacute aeacute Oslashacute oslashacute uni0218 uni0219 uni021A uni021B uni0232 uni0233 Wgrave wgrave Wacute wacute Wdieresis wdieresis Ygrave ygrave"

for glyphToRemove in glyphsToRemove.split(" "):

    #f[glyphToRemove].selected = True
    f[glyphToRemove].clear()

f.save()
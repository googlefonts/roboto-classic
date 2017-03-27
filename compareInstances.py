from AppKit import NSBezierPath
from fontTools.ttLib import TTFont
from fontTools.pens.cocoaPen import CocoaPen
import string

charset = string.uppercase+string.lowercase

label1 = "Roboto-Light"
label2 = "VF Instance"

fontpath1 = "master_ttf_interpolatable/Roboto-Bold.ttf"
fontpath2 = "instances/RobotoB-VF-instanceBold.ttf"

ttfont1 = TTFont(fontpath1)
ttfont2 = TTFont(fontpath2)

pen1 = CocoaPen(ttfont1.getGlyphSet())
pen2 = CocoaPen(ttfont2.getGlyphSet())

color1 = (1, 0, 0, 0.5)
color2 = (0, 0, 1, 0.5)

unequalmetrics = []

for char in charset:
    pen1.path = NSBezierPath.bezierPath()
    pen2.path = NSBezierPath.bezierPath()
    glyph1 = pen1.glyphSet[char]
    glyph2 = pen2.glyphSet[char]
    glyph1.draw(pen1)
    glyph2.draw(pen2)
    
    newPage(2500, 2500)
    fill(None)
    strokeWidth(2)
    offsetX = 500
    offsetY = 500
    translate(offsetX, offsetY)
    
    # baseline
    stroke(0, 0, 0, 0.25)
    line((-offsetX, 0), (width()-offsetX, 0))
    
    # glyph 1
    stroke(*color1)
    drawPath(pen1.path)
    line((0, -offsetY), (0, height()-offsetY))
    line((glyph1.width, -offsetY), (glyph1.width, 2000))
    
    # glyph 2
    stroke(*color2)
    drawPath(pen2.path)
    line((0, -offsetY), (0, height()-offsetY))
    line((glyph2.width, -offsetY), (glyph2.width, 2000))
    
    stroke(None)
    fontSize(36)

    fill(0, 0, 0, 0.5)
    text("width", (-offsetX+50, -100))    
    
    fill(*color1)
    text(label1, (-offsetX+50, height()-offsetY-100))
    text(str(glyph1.width), (-offsetX+50, -150))

    fill(*color2)
    text(label2, (-offsetX+50, height()-offsetY-150))
    text(str(glyph2.width), (-offsetX+50, -200))
    
    metricsdiff = glyph2.width - glyph1.width
    if metricsdiff != 0:
        unequalmetrics.append((char, metricsdiff))

newPage(2000, 2000)
fs = FormattedString(fontSize=30, font="Menlo")
for c, m in unequalmetrics:
    t = "%s %s\n" % (c, m)
    fs.append(t)
textBox(fs, (50, 0, width()-100, height()-50))

saveImage(["compareInstances-Bold.pdf"])



from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor
import os

###

designSpacePath = "Roboto.designspace"
familyName = "Roboto"

sources = [
	dict(path="master_ufo/Roboto-Thin.ufo", name="Roboto-Thin.ufo", location=dict(weight=100), styleName="Thin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-Light.ufo", name="Roboto-Light.ufo", location=dict(weight=300), styleName="Light", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-Regular.ufo", name="Roboto-Regular.ufo", location=dict(weight=400, width=100, slant=0), styleName="Regular", familyName=familyName, copyInfo=True),
	dict(path="master_ufo/Roboto-Medium.ufo", name="Roboto-Medium.ufo", location=dict(weight=500), styleName="Medium", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-Bold.ufo", name="Roboto-Bold.ufo", location=dict(weight=700), styleName="Bold", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-Black.ufo", name="Roboto-Black.ufo", location=dict(weight=900), styleName="Black", familyName=familyName, copyInfo=False),
	
	dict(path="master_ufo/Roboto-ThinItalic.ufo", name="Roboto-ThinItalic.ufo", location=dict(weight=100, slant=12), styleName="Thin Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-LightItalic.ufo", name="Roboto-LightItalic.ufo", location=dict(weight=300, slant=12), styleName="Light Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-Italic.ufo", name="Roboto-Italic.ufo", location=dict(slant=12), styleName="Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-MediumItalic.ufo", name="Roboto-MediumItalic.ufo", location=dict(weight=500, slant=12), styleName="Medium Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-BoldItalic.ufo", name="Roboto-BoldItalic.ufo", location=dict(weight=700, slant=12), styleName="Bold Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Roboto-BlackItalic.ufo", name="Roboto-BlackItalic.ufo", location=dict(weight=900, slant=12), styleName="Black Italic", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoCondensed-Light.ufo", name="RobotoCondensed-Light.ufo", location=dict(weight=300, width=75), styleName="Condensed Light", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoCondensed-Regular.ufo", name="RobotoCondensed-Regular.ufo", location=dict(width=75), styleName="Condensed Regular", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoCondensed-Bold.ufo", name="RobotoCondensed-Bold.ufo", location=dict(weight=700, width=75), styleName="Condensed Bold", familyName=familyName, copyInfo=False),

	dict(path="master_ufo/RobotoCondensed-LightItalic.ufo", name="RobotoCondensed-LightItalic.ufo", location=dict(weight=300, width=75, slant=12), styleName="Condensed Light Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoCondensed-Italic.ufo", name="RobotoCondensed-Italic.ufo", location=dict(width=75, slant=12), styleName="Condensed Italic", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/RobotoCondensed-BoldItalic.ufo", name="RobotoCondensed-BoldItalic.ufo", location=dict(weight=700, width=75, slant=12), styleName="Condensed Bold Italic", familyName=familyName, copyInfo=False),
]
axes = [
	dict(minimum=100, maximum=900, default=400, name="weight", tag="wght", labelNames={"en": "Weight"}, map=[]),
	dict(minimum=75, maximum=100, default=100, name="width", tag="wdth", labelNames={"en": "Width"}, map=[]),
	dict(minimum=0, maximum=12, default=0, name="slant", tag="slnt", labelNames={"en": "Slant"}, map=[]),
]

instances = []

for source in sources:
	instances.append(dict(location=source["location"], styleName=source["styleName"], familyName=source["familyName"]))


### 

doc = DesignSpaceDocument()

for source in sources:
	s = SourceDescriptor()
	s.path = source["path"]
	s.name = source["name"]
	s.copyInfo = source["copyInfo"]
	s.location = source["location"]
	s.familyName = source["familyName"]
	s.styleName = source["styleName"]
	doc.addSource(s)

for instance in instances:
	i = InstanceDescriptor()
	i.location = instance["location"]
	i.familyName = instance["familyName"]
	i.styleName = instance["styleName"]
	doc.addInstance(i)

for axis in axes:
	a = AxisDescriptor()
	a.minimum = axis["minimum"]
	a.maximum = axis["maximum"]
	a.default = axis["default"]
	a.name = axis["name"]
	a.tag = axis["tag"]
	for languageCode, labelName in axis["labelNames"].items():
		a.labelNames[languageCode] = labelName
	a.map = axis["map"]
	doc.addAxis(a)

#doc.checkAxes()

#doc.checkDefault()

doc.write(designSpacePath)

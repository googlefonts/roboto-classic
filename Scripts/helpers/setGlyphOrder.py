from defcon.objects.font import Font
import os

glyphOrder = []

with open("glyphorder.txt", "r") as f:
	glyphOrder = f.read().splitlines()

DIR = "master_ufo"

for fn in os.listdir(DIR):
	if fn.endswith(".ufo"):
		font = Font(os.path.join(DIR, fn))
		font.glyphOrder = glyphOrder
		font.save()
		print fn
print "Done"

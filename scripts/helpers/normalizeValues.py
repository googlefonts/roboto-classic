
userValue = 600
axisDefault = 400

axisMin = 100
axisMax = 900


if (userValue < axisDefault):
	normalizedValue = (userValue - axisDefault) / (axisDefault - axisMin)
else:
	normalizedValue = (userValue - axisDefault) / (axisMax - axisDefault)
	
print(normalizedValue)
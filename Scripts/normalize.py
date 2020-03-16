intMin = 100
intMax = 900

intLocation = 100

intMin = -1
intMax = 1

normalized_x = int ( 2 * int ( int (intLocation - intMin) / int (intMax - intMin) ) ) - 1

print ( normalized_x )

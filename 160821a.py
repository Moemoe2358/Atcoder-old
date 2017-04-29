a = raw_input()
n, w, s, e = -1, -1, -1, -1

for i in a:
	if i == "S":
		s = 1
	if i == "W":
		w = 1
	if i == "E":
		e = 1
	if i == "N":
		n = 1

if w * e > 0 and n * s > 0:
	print "Yes"
else:
	print "No"
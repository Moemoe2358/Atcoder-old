import sys

a = raw_input()

for i in a:
	s = 0
	for j in a:
		if i == j:
			s += 1 
	if s % 2 == 1:
		print "No"
		sys.exit()

print "Yes"
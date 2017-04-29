a = raw_input()
s = ""

for i in a:
	if i == "0" or i == "1":
		s += i
	else:
		s = s[:len(s) - 1]

print s
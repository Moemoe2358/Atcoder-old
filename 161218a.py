s = raw_input()

a = s.find('+')
ok = 0
if a == -1:
	a = s.find('-')
	ok = 1

n1 = int(s[:(a - 1)])
n2 = int(s[(a + 1):])

if ok == 0:
	print n1 + n2
else:
	print n1 - n2
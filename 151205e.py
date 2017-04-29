from collections import Counter
s = input()
for h in range(s):
	l = raw_input().split()
	s0 = l[0]
	s1 = l[1]
	l = []
	for i in s1:
		l.append(i)
	l = list(set(l))
	for i in range(97,123):
		c = chr(i)
		if c not in l:
			s0 = s0.translate(None,c)
	if s1 in s0:
		print "YES"
	else:
		print "NO"

n = input()
l1 = []

for i in range(n):
	t = input()
	l1.append(t)

l2 = sorted(l1)

s1, s2 = set([]), set([])

for i in range(n):
	if i % 2 == 1:
		s1.add(l1[i])
		s2.add(l2[i])

print len(s1) - len(s1.intersection(s2))

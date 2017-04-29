n = input()

l = []
for i in range(n):
	t = input()
	l.append(t)

ll = list(set(l))
ll.sort()

d = {}
t = 0
for i in range(len(ll)):
	d[ll[i]] = i

for i in range(n):
	print d[l[i]]
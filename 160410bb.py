n = input()

a = map(int, raw_input().split())
for i in range(len(a)):
	a[i] = a[i] - 1
b = [i for i in range(len(a))]

d = {}
for i in range(len(a)):
	d[b[i]] = a[i]

s = 0

while len(b) > 0:
	c = []
	c.append(b[0])
	t = d[b[0]]
	b.remove(b[0])
	while t not in c:
		c.append(t)
		b.remove(t)
		t = d[t]
		
	s += 1

print s
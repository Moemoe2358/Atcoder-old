k = input()
a1, a2 = map(int, raw_input().split())

s1 = a1 / float(a1 + a2)
s2 = a2 / float(a1 + a2)

s = 0
c1 = s1 * s2
c2 = s2 * s1

for i in range(2,10000):
	s = s + (c1 + c2) * i
	c1 = c1 * s1
	c2 = c2 * s2

print s
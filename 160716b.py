n, x = map(int, raw_input().split())

s = 0
t = n - x
while t % x != 0:
	m = t % x
	s += x * (t / x)
	t = x
	x = m
s += x * (t / x)

print s * 3
n, q = map(int, raw_input().split())

a = [0 for _ in range(n + 1)]

for _ in range(q):
	l, r, t = map(int, raw_input().split())
	for i in range(l, r + 1):
		a[i] = t

for i in range(1, n + 1):
	print a[i]
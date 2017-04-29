n = input()
t = map(int, raw_input().split())
s = sum(t)

m = input()
for i in range(m):
	p, x = map(int, raw_input().split())
	print s - t[p - 1] + x
n, m = map(int, raw_input().split())
a = raw_input()
s = 1
k = 0
for i in range(n):
	if a[i] == '+':
		s += 1
	else:
		s -= 1
	if s > m:
		k += 1
		s = 1
print k
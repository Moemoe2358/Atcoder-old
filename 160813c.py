a = input()
l = map(int, raw_input().split())

s = 100000000
ma = max(l)
mi = min(l)

for i in range(mi, ma + 1):
	t = 0
	for j in l:
		t += (j - i) ** 2
	if t < s:
		s = t

print s
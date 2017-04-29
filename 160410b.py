n = input()

a = map(int, raw_input().split())
for i in range(len(a)):
	a[i] = a[i] - 1
b = [0 for i in range(len(a))]

s = 0

for i in range(len(a)):
	if b[i] == 0:
		d = []
		d.append(i)
		t = a[i]
		while t not in d:
			d.append(t)
			t = a[t]
		s += 1
		for i in range(len(d)):
			b[d[i]] = 1

print s
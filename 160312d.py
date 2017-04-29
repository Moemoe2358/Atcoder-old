n, k = map(int, raw_input().split())

a = []
b = []

for i in range(n):
	ta, tb = map(int, raw_input().split())
	a.append(ta)
	b.append(tb)

l = 0
s = 0

for i in range(k):
	ma = 0
	k = 0
	for j in range(n - i):
		templ = l + a[j]
		temps = s + a[j] * b[j] / float(100)
		temp = temps / templ
		if temp > ma:
			ma = temp
			k = j
	l = l + a[k]
	s = s + a[k] * b[k] / float(100)
	del a[k], b[k]

print s / l * 100

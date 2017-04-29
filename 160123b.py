from __future__ import print_function
a = input()
l = map(int, raw_input().split())

y = []
y.append(l[0])

for i in range(1, a - 1):
	if l[i] > l[i - 1]:
		y.append(l[i - 1])
	elif l[i] == l[i - 1]:
		y.append(l[i - 1])
	elif l[i] < l[i - 1]:
		y.append(l[i])

y.append(l[a - 2])

for i in range(a):
	print (y[i], end = " ")
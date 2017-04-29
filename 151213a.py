m = input()
r = m % 9
d = m / 9
if r == 0:
	r = 9
	d = d - 1
s = 0
for i in range(d + 1):
	s = s * 10 + r
print s
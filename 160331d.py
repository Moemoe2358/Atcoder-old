def add0(a):
	if len(a) == 1:
		a = "0" + a
	return a

n = input()
l = [0 for i in range(289)]

for i in range(n):
	s = raw_input()
	a = int(s[0:4])
	a = a / 100 * 12 + a % 100 / 5
	b = int(s[5:9])
	b = b / 100 * 12 + (b % 100 - 1) / 5
	for j in range(a, b + 1):
		l[j] = 1

flag = 0
i = 0
while i < 289:
	if l[i] == 1 and flag == 0:
		flag = 1
		start = i
	if l[i] == 0 and flag == 1:
		flag = 0
		end = i
		o1 = str(start / 12) 
		o2 = str(start % 12 * 5)
		o3 = str(end / 12)
		o4 = str(end % 12 * 5)
		print add0(o1) + add0(o2) + "-" + add0(o3) + add0(o4)
	i += 1


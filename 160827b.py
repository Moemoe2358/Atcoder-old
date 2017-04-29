a = raw_input()
l = len(a)
s = 0
n = 0

left = 0
right = 0

# for i in range(l):
# 	if i == '(':
# 		left += 1
# 	else:
# 		right += 1

# t = abs((left - right) / 2)

e, f = 0, 0

for i in reversed(range(l)):
	if a[i] == '(':
		s -= 1
	else:
		s += 1
	if s < 0:
		a = a[:i] + ')' + a[i + 1:]
		s += 2
		e += 1
		if i > n:
			n = i

for i in a:
	if i == '(':
		left += 1
	else:
		right += 1

t = abs((left - right) / 2)

s = 0
if t > 0:
	for i in range(l):
		if a[i] == ')':
			s += 1
			if s == t and i > n:
				n = i
				break

print n + e + t
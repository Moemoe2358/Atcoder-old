s = raw_input()
t = input()
x, y, z = 0, 0, 0

if t == 1:
	for i in range(len(s)):
		if s[i] == 'L':
			x -= 1
		if s[i] == 'R':
			x += 1
		if s[i] == 'U':
			y += 1
		if s[i] == 'D':
			y -= 1
		if s[i] == '?':
			z += 1
	print abs(x) + abs(y) + z

if t == 2:
	for i in range(len(s)):
		if s[i] == 'L':
			x -= 1
		if s[i] == 'R':
			x += 1
		if s[i] == 'U':
			y += 1
		if s[i] == 'D':
			y -= 1
		if s[i] == '?':
			z += 1
	r = abs(x) + abs(y) - z
	if r >= 0:
		print r
	elif abs(r) % 2 == 1:
		print 1
	else:
		print 0
a, b, c = map(int, raw_input().split())

x = []
t = [1 for a in range(a + 1)]

for _ in range(b):
	z = map(int, raw_input().split())
	l = []
	x.append(z)
	# for tt in x:
	# 	if z[0] == tt[0] and [z[1], tt[1]] not in x:
	# 		l.append([z[1],tt[1]])
	# 	if z[1] == tt[1] and [z[0],tt[0]] not in x:
	# 		l.append([z[0],tt[0]])
	# 	if z[0] == tt[1] and [z[1],tt[0]] not in x:
	# 		l.append([z[1],tt[0]])
	# 	if z[1] == tt[0] and [z[0],tt[1]] not in x:
	# 		l.append([z[0],tt[1]])
	# x = x + l
	# xq = []
	# for tt in x:
	# 	if tt not in xq:
	# 		xq.append(tt)
	# x = xq

for _ in range(c):
	z = map(int, raw_input().split())
	if z in x:
		t[z[0]] += 1
		t[z[1]] += 1
	elif [z[1], z[0]] in x:
		t[z[0]] += 1
		t[z[1]] += 1
# print x
for i in range(1, a + 1):
	print t[i],


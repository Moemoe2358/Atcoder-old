n, m = map(int, raw_input().split())

machi = [[0 for i in range(n)] for j in range(n)]

for h in range(m):
	a, b, c = map(int, raw_input().split())
	for i in range(c):
		for j in range(i + 1):
			machi[a + i - 1][b + j - 1] = 1

q = input()

for h in range(q):
	s = 0
	a, b, c = map(int, raw_input().split())
	# for i in range(c):
	# 	for j in range(i + 1):
	# 		if machi[a + i - 1][b + j - 1] == 0:
	# 			s += 1
	for j in range(c):
		s += machi[a+j-1][b+0-1:b+j].count(0)
	print s

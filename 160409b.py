n = input()
m = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
	q = raw_input()
	for j in range(n):
		m[i][j] = q[j]

mm = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
	for j in range(n):
		mm[j][n - i - 1] = m[i][j]

for i in range(n):
	s = ""
	for j in range(n):
		s = s + mm[i][j]
	print s
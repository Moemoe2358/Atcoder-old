w, h = map(int, raw_input().split())

m = [[0 for i in range(w)] for j in range(h)]

for i in range(h):
	for j in range(w):
		if i == 0 or j == 0:
			m[i][j] = 1
		else:
			m[i][j] = m[i - 1][j] + m[i][j - 1]

print m[h - 1][w - 1] % 1000000007
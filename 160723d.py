h, w, a, b = map(int, raw_input().split())

m = [1 for _ in range(w)]

for _ in range(h - a - 1):
	for j in range(1, w):
		m[j] = m[j] + m[j - 1]

for _ in range(a):
	for j in range(b + 1, w):
		m[j] = m[j] + m[j - 1]	

print m[w - 1]


# for i in range(a):
# 	for j in range(b):
# 		m[h - i - 1][j] = -1

# for i in range(w):
# 	m[0][i] = 1

# for i in range(h - a):
# 	m[i][0] = 1

# for i in range(a):
# 	m[h - i - 1][b] = 1

# for i in range(1, h):
# 	for j in range(1, w):
# 		if m[i][j] != -1 and m[i][j - 1] != -1:
# 			m[i][j] = m[i - 1][j] + m[i][j - 1]
# 		if m[i][j] != -1 and m[i][j - 1] == -1:
# 			m[i][j] = m[i - 1][j]

# print m[h - 1][w - 1]

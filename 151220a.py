def pr(a):
	for i in range(h):
		s = ""
		for j in range(w):
			if a[i][j] == 2:
				s = s + "#"
			else:
				s = s + "."
		print s

h, w, k = map(int, raw_input().split())
a = [[0 for j in range(w)] for i in range(h)]

n = 0
for i in range(h):
	for j in range(w):
		if a[i][j] == 0:
			n = n + 1
			a[i][j] = 2
			if i + 1 < h:
				a[i + 1][j] = 1
			if j + 1 < w:
				a[i][j + 1] = 1
			if i + 1 < h and j + 1 < w:
				a[i + 1][j + 1] = 1
		if n == k:
			pr(a)
			n = n + 1
			break
if n < k:
	print "IMPOSSIBLE"

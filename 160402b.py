r, b = map(int, raw_input().split())
x, y = map(int, raw_input().split())
t = r / x
ma = 0

for i in range(t + 1):
	j = min((b - i) / y, r - i * x)
	if i + j > ma:
		ma = i + j
		print i, j

print ma
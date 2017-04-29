a, b, c = map(int, raw_input().split())
ma = 0

for i in range(c / a + 1):
	ma = max((c - i * a) / b + i, ma)

print ma
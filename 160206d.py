def dis(x1, y1, x2, y2):
	return pow(x1 - x2, 2) + pow(y1 - y2, 2)

n = input()
q1, q2, q3 = 0, 0, 0
x = []
y = []

for i in range(n):
	tx, ty = map(int, raw_input().split())
	x.append(tx)
	y.append(ty)

for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			c1 = dis(x[i], y[i], x[j], y[j])
			c2 = dis(x[i], y[i], x[k], y[k])
			c3 = dis(x[k], y[k], x[j], y[j])
			if (c2 > c1) and (c2 > c3):
				t = c1
				c1 = c2
				c2 = t
			if (c3 > c1) and (c3 > c2):
				t = c1
				c1 = c3
				c3 = t
			if c1 < c2 + c3:
				q1 += 1
			if c1 == c2 + c3:
				q2 += 1
			if c1 > c2 + c3:
				q3 += 1

print q1, q2, q3
n, x, y = map(int, raw_input().split())
ma = min(y * 50, 10001)
dp = [[-1 for j in range(ma)] for i in range(n + 1)]

dp[0][0] = 0

for i in range(n):
	a, b = map(int, raw_input().split())
	for j in reversed(range(i + 1)):
		for k in range(ma):
			if dp[j][k] != -1:
				dp[j + 1][min(ma, k + b)] = max(dp[j + 1][min(ma, k + b)], dp[j][k] + a + b)

for i in range(1, n + 1):
	for j in range(y, ma):
		if dp[i][j] >= (x + y):
			print i
			dp[0][0] = -1
			break
	if dp[0][0] == -1:
		break
if dp[0][0] == 0:
	print -1
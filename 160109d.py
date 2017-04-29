n, l = map(int, raw_input().split())
ma = l * 200 + 5
dp = [-1 for j in range(ma)]

for i in range(n):
	v, w = map(int, raw_input().split())
	for j in reversed(range(ma)):
		if dp[j] != -1:
			dp[min(ma, j + w)] = max(dp[min(ma, j + w)], dp[j] + v)
	dp[w] = v

dp[0] = 0

for i in reversed(range(l + 1)):
	if dp[i] != -1:
		print dp[i]
		break

print dp
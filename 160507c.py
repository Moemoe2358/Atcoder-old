n, k = map(int, raw_input().split())
l = map(int, raw_input().split())

s = 0
t = 0

for i in range(n):
	if i < n - k + 1:
		t += 1
	if i >= k:
		t -= 1
	s = s + l[i] * t

print s


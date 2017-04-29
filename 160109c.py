n, k = map(int, raw_input().split())
l = []

for i in range(n):
	s = input()
	if s == 0:
		print n
		exit(0)
	l.append(s)

p = 1
left = 0
ma = 0

for right in range(n):
	p *= l[right]
	if p > k:
		p = p / l[left]
		left += 1
	ma = max(ma, right - left + 1)
print ma
	
# import bisect
n, m = map(int, raw_input().split())
mal = [map(int, raw_input().split()) for loop in xrange(n)]
fem = [map(int, raw_input().split()) for loop in xrange(m)]

mal.sort()
fem.sort(key=lambda x:(x[1]))

success = 0
s = []
j = 0

for i in range(n):
	while j <= m - 1 and fem[j][1] <= mal[i][0]:
		s.append(fem[j][0])
		j += 1
	mini = 10000000001
	a = len(s)
	for k in range(len(s)):
		if s[k] >= mal[i][1] and s[k] < mini:
			mini = s[k]
			a = k
	# s.sort()
	# a = bisect.bisect_left(s,mal[i][1])
	if (a != len(s)):
		success += 1
		s[a] = 10000000001

print success
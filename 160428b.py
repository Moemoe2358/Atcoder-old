s = raw_input()
m = input()

for _ in range(m):
	t = int(s[0])
	s = s[1:t] + s[0] + s[t::]
	print s 
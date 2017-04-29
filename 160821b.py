n = input()
rest = 0
s = 0

for _ in range(n):
	t = input()
	if t != 0:
		t += rest
	s += t / 2
	if t % 2 == 1:
		rest = 1
	else:
		rest = 0

print s
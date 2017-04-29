n = input()
l = map(int, raw_input().split())

l.sort()

s = 0

for i in range(len(l)):
	if i % 2 == 0:
		s += l[i]

print s
n, l = map(int, raw_input().split())

l = []

for i in range(n):
	l.append(raw_input())

l.sort()

s = ""
for i in range(n):
	s += l[i]

print s
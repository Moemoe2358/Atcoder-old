a, b = map(int, raw_input().split())
b += 1
l = map(int, raw_input().split())

s = 0
for i in l:
	if i > b:
		s += b
	else:
		s += i

print s
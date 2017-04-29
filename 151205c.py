s = input()
l = map(int, raw_input().split())
l.append(999)
t = input()
# print l,t
for i in range(s + 1):
	if t < l[i]:
		print i + 1
		break
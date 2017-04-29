l = map(int, raw_input().split())
a1 = l[0]
a2 = l[1]
l = map(int, raw_input().split())
b1 = l[0]
b2 = l[1]
t = input()
# print a1,a2,b1,b2,t
l = []
if a1 == t or a2 == t:
	l.append(b1)
	l.append(b2)
if b1 == t or b2 == t:
	l.append(a1)
	l.append(a2)
l = list(set(l))
l.sort()
print len(l)
for i in l:
	print(i)
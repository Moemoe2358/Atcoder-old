m = input()
s = []
s.append(0)
for i in range(m):
    s.append(input())
su = sum(s)
n = input()
a = []
a.append(0)
b = []
b.append(0)
for i in range(n):
	l = map(int, raw_input().split())
	if l[0] == 0:
		a.append(l[1])
		b.append(l[2])
	else:
		ss = []
		pp = []
		ss.append(s[l[1]])
		pp.append(l[1])
		for j in range(len(a)):
			if l[1] == a[j]:
				ss.append(s[b[j]])
				pp.append(b[j])
		if l[2] in pp:
			print s[l[2]],s[l[2]]
		else:
			r = su - sum(ss)
			if len(ss) == m - 1:
				print r,r
			else:
				print max(0,r - 100 * (m - len(ss) - 1)),min(r,100)

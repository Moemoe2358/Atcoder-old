l = map(int, raw_input().split())
m = l[0]
n = l[1]
a = []
b = []
c = []
d = []
for i in range(m):
	l = map(int, raw_input().split())
	a.append(l[0])
	b.append(l[1])
for i in range(n):
	l = map(int, raw_input().split())
	c.append(l[0])
	d.append(l[1])
d.sort()
a.sort()

# it will cost lot if use del 

i, j = 0, 0
s = 0
while len(a) > i and len(d) > j:
	if a[i] >= d[j]:
		s += 1
		i += 1
		j += 1
	else:
		i += 1
print s

# N, M = map(int, raw_input().split())
# mal = [map(int, raw_input().split()) for loop in xrange(N)]
# fem = [map(int, raw_input().split()) for loop in xrange(M)]
 
# A = [m[0] for m in mal]
# D = [f[1] for f in fem]
 
# A.sort()
# D.sort()
# print A, D,mal,fem
# print ""
# print mal[0][0],fem[1][1],str(3) * 5
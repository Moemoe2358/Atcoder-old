import sys

n = input()
c = []
p = []

for i in range(n):
	k = raw_input().split()
	c.append(k[0])
	p.append(int(k[1]))

s = sum(p)

for i in range(n):
	if p[i] > float(s) / 2:
		print c[i]
		sys.exit()

print "atcoder"


import random
from sets import Set

k = input()
a = map(int, raw_input().split())
l = []

for i in range(k):
	for j in range(a[i]):
		l.append(i)

s = Set([])
for i in range(0, k):
	s.add(i)

su = 0
for i in range(100000):
	ss = Set([])
	time = 0
	while s != ss:
		time += 1
		ss.add(random.choice(l))
	su += time

print su / float(100000)
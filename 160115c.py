import random
l = [0, 1, 2]
aa = input()
s = 0

for h in range(200000):
	n = 0
	ll = []
	for i in range(aa):
		ll.append(random.choice(l))
	a = aa
	while len(ll) > 1:
		n += 1

		a0 = ll.count(0)
		a1 = ll.count(1)
		a2 = ll.count(2)
		if a0 == 0:
			a = a1
		if a1 == 0:
			a = a2
		if a2 == 0:
			a = a0
		if a0 != 0 and a1 != 0 and a2 != 0:
			if a0 == a1 and a1 > a2:
				a = a2
			if a0 == a2 and a2 > a1:
				a = a1
			if a1 == a2 and a1 > a0:
				a = a0
			if a0 == a1 and a1 < a2:
				a = a0
			if a0 == a2 and a2 < a1:
				a = a2
			if a1 == a2 and a1 < a0:
				a = a1
		ll = []
		for i in range(a):
			ll.append(random.choice(l))
	s += n

print s / 200000.0
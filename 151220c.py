n = input()
l = []
a = 0
for i in range(n):
	s1 = raw_input()
	s2 = raw_input()
	s3 = raw_input()
	if i % 2 == 0:
		if s1 == "###":
			l.append(2)
		if s1 == ".##":
			l.append(1)
			a += 1
		if s1 == "##.":
			l.append(1)
			a += 1
		if s1 == ".#.":
			a += 2
		if s1 == "#.#":
			a += 1
	if i % 2 == 1:
		if s1 == "###" and s2 == "###" and s3 == "###":
			l.append(2)
		if s1 == "..." and s2 == "###" and s3 == "###":
			l.append(1)
			a += 1
		if s1 == "###" and s2 == "###" and s3 == "...":
			l.append(1)
			a += 1
		if s1 == "..." and s2 == "###" and s3 == "...":
			a += 2
		if s1 == "###" and s2 == "..." and s3 == "###":
			a += 1

l1 = l.count(1)
l2 = l.count(2)

if l1 % 2 == 0 and l2 % 2 == 0:
	f = 2 
else:
	f = 1

if a % 2 == 0 and f == 1 or a % 2 == 1 and f == 2:
	print "Snuke"
else:
	print "Sothe"
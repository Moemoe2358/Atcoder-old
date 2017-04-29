n = input()
a = map(int, raw_input().split())
a.sort()
ok = 0
# print a

if n % 2 == 1:
	for i in range(len(a)):
		if (i % 2 == 0 and a[i] != i) or (i % 2 == 1 and a[i] != i + 1):
			print 0
			ok = 1
			break

if n % 2 == 0:
	for i in range(len(a)):
		if (i % 2 == 1 and a[i] != i) or (i % 2 == 0 and a[i] != i + 1):
			print 0
			ok = 1
			break

if ok == 0:
	# print pow(2, n / 2)
	print pow((2 % 1000000007), ((n / 2) % 1000000006)) % 1000000007
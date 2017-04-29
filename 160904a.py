a, b, c = map(int, raw_input().split())

if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
	if a >= b and a >= c:
		print b * c
	elif b >= c and b >= a:
		print a * c
	elif c >= a and c >= b:
		print a * b
else:
	print 0
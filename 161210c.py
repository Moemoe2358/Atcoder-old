a = raw_input()

t = ['dream', 'dreamer', 'erase', 'eraser']

while len(a) > 0:
	if a[:7] == 'dreamer' and a[:8][-1] != 'a':
		a = a[7:]
	elif a[:6] == 'eraser':
		a = a[6:]
	elif a[:5] in ['dream', 'erase']:
		a = a[5:]
	else:
		print "NO"
		break

if len(a) == 0:
	print "YES"

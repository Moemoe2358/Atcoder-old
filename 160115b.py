a = raw_input()
f = 0
i = 0
s = 0
while 1:
	if a[i] == '2' and a[i + 1] == '5':
		f += 1
		i += 2
	else:
		s = s + (f * (f + 1) / 2)
		i += 1
		f = 0
	if i + 1 >= len(a):
		break
s = s + (f * (f + 1) / 2)
print s

	
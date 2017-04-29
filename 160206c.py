n = raw_input()
i = 1

while i < len(n) - 1:
	if (n[i] == '*'):
		if (n[i - 1] == '0') or (n[i + 1] == '0'):
			n = n[0 : i - 1] + '??0' + n[i + 2 : len(n)]
		else:
			n = n[0 : i - 1] + '??1' + n[i + 2 : len(n)]
	i += 2

s = 0
for i in range(len(n)):
	if (n[i] >= '1') and (n[i] <= '9'):
		s += 1

print s



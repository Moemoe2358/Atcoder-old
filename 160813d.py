import sys
s = raw_input()

for i in range(len(s) - 1):
	if s[i] == s[i + 1]:
		print i + 1, i + 2
		sys.exit()

if len(s) >= 2:
	for i in range(len(s) - 2):
		if s[i] == s[i + 2]:
			print i + 1, i + 3
			sys.exit()

print -1, -1
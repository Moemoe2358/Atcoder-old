s = raw_input()

p = 0
for i in range(len(s)):
	if s[i] == ",":
		print s[p:i]
		p = i + 1

print s[p::]
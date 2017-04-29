s = raw_input()
k = input()
l = []
for i in range(len(s) - k + 1):
	ll = s[i:i + k]
	l.append(ll)
l = set(l)
print len(l)
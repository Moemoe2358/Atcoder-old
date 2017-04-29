def dis(dic, dics):
	s = 0
	s = s + abs(dic['a'] - dics['a'])
	s = s + abs(dic['b'] - dics['b'])
	s = s + abs(dic['c'] - dics['c'])
	s = s + abs(dic['d'] - dics['d'])
	return s

l = ['a', 'b', 'c', 'd']
s = raw_input()

dic = {'a':0, 'b':0, 'c':0, 'd':0}

for i in range(len(s)):
	dic[s[i]] = dic[s[i]] + 1

if len(s) == 1:
	for i in range(len(l)):
		ss = l[i]
		dics = {'a':0, 'b':0, 'c':0, 'd':0}
		dics[ss[0]] = dics[ss[0]] + 1
		if dis(dic, dics) == 0 or dis(dic, dics) == 2:
			print ss

if len(s) == 2:
	for i in range(len(l)):
		for j in range(len(l)):
			ss = l[i] + l[j]
			dics = {'a':0, 'b':0, 'c':0, 'd':0}
			for p in range(len(ss)):
				dics[ss[p]] = dics[ss[p]] + 1
			if dis(dic, dics) == 0 or dis(dic, dics) == 2:
				print ss

if len(s) == 3:
	for i in range(len(l)):
		for j in range(len(l)):
			for k in range(len(l)):
				ss = l[i] + l[j] + l[k]
				dics = {'a':0, 'b':0, 'c':0, 'd':0}
				for p in range(len(ss)):
					dics[ss[p]] = dics[ss[p]] + 1
				if dis(dic, dics) == 0 or dis(dic, dics) == 2:
					print ss


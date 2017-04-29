n, k = map(int, raw_input().split())

l = map(int, raw_input().split())
flag = False

while flag == False:
	flag = True
	t = n
	while t > 0:
		m = t % 10
		if m in l:
			flag = False
			break
		t = t / 10
	n += 1

print n - 1
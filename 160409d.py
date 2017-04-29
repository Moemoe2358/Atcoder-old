n = input()

a, b = [], []
for i in range(n - 1):
	ta, tb = map(int, raw_input().split())
	a.append(ta - 1)
	b.append(tb - 1)

s = "0" * n
count = 1
while (s != "1" * n):
	p = -1
	t = s[p]
	while t == "1":
		p = p - 1
		t = s[p]
	s = s[:p] + "1" + "0" * (-1 - p)
	flag = 1
	for j in range(n - 1):
		if (s[a[j]] == "1") and (s[b[j]] == "1"):
			flag = 0
	if flag == 1:
		count += 1

print count
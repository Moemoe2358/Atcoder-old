a = raw_input()

s = 0
flag = 0

for i in range(len(a)):
	if a[i] == "I" and flag == 0:
		flag = 1
		s = s + 1
	if a[i] == "O" and flag == 1:
		flag = 0
		s = s + 1

if s % 2 == 0:
	s = s - 1

if s < 1:
	s = 0

print s
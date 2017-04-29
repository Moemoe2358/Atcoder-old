m = input()
# arr = [[0 for i in range(2)] for j in range(m)]
# for i in range(m):
# 	l = map(int, raw_input().split())
# 	arr[i][0] = l[0]
# 	arr[i][1] = l[1]
n = 0
a = []
for i in range(m - 1):
    a.append(map(int, raw_input().split()))
for i in a:
	if 1 in i:
		n = n + 1
if n == 1:
	print("A")
else:
	if m % 2 == 0:
		print("A")
	else:
		print("B")

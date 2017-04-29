#60点
# n, q = map(int, raw_input().split())
# m = [0 for i  in range(n + 1)]

# for i in range(q):
# 	l, r = map(int, raw_input().split())
# 	for j in range(l, r + 1):
# 		if m[j] == 0:
# 			m[j] = 1
# 		else:
# 			m[j] = 0

# s = ""
# for i in range(1, n + 1):
# 	s += str(m[i])
# print s

#満点
n, q = map(int, raw_input().split())
m = [0 for i  in range(n + 2)]

for i in range(q):
	l, r = map(int, raw_input().split())
	m[l] += 1
	m[r + 1] -= 1

su = 0
s = ""
for i in range(1, n + 1):
	su += m[i]
	s += str(su % 2)
print s
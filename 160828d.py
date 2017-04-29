import sys

def f(b, n):
	if n < b:
		return n
	return f(b, n / b) + n % b

# print f(31434, 1)
n = input()
s = input()

for i in range(2, n - 1):
	if f(i, n) == s:
		print i
		sys.exit()

print -1
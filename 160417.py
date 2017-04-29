def f(n):
	if n == 1 or n == 2:
		return 1
	a1 = 1
	a2 = 1
	for _ in range(n - 2):
		a3 = a2 + a1
		a1 = a2
		a2 = a3
	return a3

a = input()
print f(a)
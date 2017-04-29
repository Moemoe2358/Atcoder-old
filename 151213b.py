m = input()
l = map(int, raw_input().split())
a = l[0]
b = l[1]
if a == b:
	if m % (b + 1) == 0:
		print("Aoki")
	else:
		print("Takahashi")
if a > b:
	print("Takahashi")
if a < b:
	if m <= a:
		print("Takahashi")
	else:
		print("Aoki")
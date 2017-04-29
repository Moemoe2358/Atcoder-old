s1 = input()
s2 = input()
if s1 * s2 < 0:
	print abs(s1 - s2) * 2
else:
	print max(abs(s1),abs(s2)) * 2
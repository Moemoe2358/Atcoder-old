def delete(a, c):
	return a.replace(c, "")

a = raw_input()
a = delete(a, "a")
a = delete(a, "e")
a = delete(a, "i")
a = delete(a, "o")
a = delete(a, "u")

print a
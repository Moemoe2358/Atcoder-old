m = input()
m = m / float(1000)

if m < 0.1:
	w = "00"
elif m <= 5:
	w = str(int(m * 10))
	if len(w) == 1:
		w = "0" + w
elif m <= 30:
	w = str(int(m + 50))
elif m <= 70:
	w = str(int((m - 30) / 5 + 80))
else:
	w = "89"

print w
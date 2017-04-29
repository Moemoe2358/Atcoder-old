l = ["NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
ll = [2,15,33,54,79,107,138,171,207,244,284,326]
a, b = map(int, raw_input().split())

a = a / float(10)
if a < 11.25:
	a += 360
a = int(round(a / float(22.5)))
e = l[a - 1]

b = round(b / float(6))
s = len(ll)
for i in range(len(ll)):
	if b <= ll[i]:
		s = i
		break

if s == 0:
	e = "C"

print e, s
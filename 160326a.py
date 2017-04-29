w, h = map(int, raw_input().split())

if float(w) / 16 == float(h) / 9:
	print "16:9"
else:
	print "4:3"  
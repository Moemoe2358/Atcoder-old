def solution(N):	
	# count how many times every digit appears on N, and save it into a list
	list_N = [0 for _ in range(10)]
	temp_N = N
	while temp_N > 0:
		mod = temp_N % 10
		list_N[mod] += 1
		temp_N = temp_N / 10
	
	#set the search range
	counter = 0
	range_begin = 10**(len(str(N)) - 1) - 1
	range_end = 10**len(str(N))

	print list_N
	# brute-force search every integer in the range designed and do the same job above on them
	for i in range(range_begin, range_end):
		list_i = [0 for _ in range(10)]
		temp_i = i
		while temp_i > 0:
			mod = temp_i % 10
			list_i[mod] += 1
			temp_i = temp_i / 10	
		
		# compare the 2 lists to show if they are same. If same, the counter +1
		flag = 1
		for j in range(10):
			if list_i[j] != list_N[j]:
				flag = 0
				break
		if flag == 1:
			counter += 1
		print list_i
	return counter

inp = input()
print solution(inp)
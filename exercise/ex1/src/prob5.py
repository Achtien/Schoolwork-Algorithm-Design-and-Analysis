def select_books(d, a, m):
	'''
	Parameter:
		d: the difficulty indices of the books in shelf order.
		a: the student's reading ability.
		m: the number of books the student must select.

	Return:
		result: a list contains indices of the selected books.
	'''
	def choose_min(n0, n1):
		if n0 == '#':
			return 1
		elif n1 == '#':
			return 0
		elif type(n0).__name__ == type(n1).__name__ == 'int':
			if n0 <= n1:
				return 0
			else:
				return 1
		elif n0[1] < n1[1]:
			return 0
		elif n0[1] == n1[1]:
			if n0[0] < n1[0]:
				return 0
			elif n0[0] > n1[0]:
				return 1
			else:
				 print('wrong')
		elif n0[1] > n1[1]:
			return 1
		else:
			print('wrong')

	def sort(d):
		n = len(d)
		if n == 0 or n == 1:
			return d
		res = []

		# divide	
		d0 = d[:n//2]
		d1 = d[n//2:]
		
		# conquer
		d0 = sort(d0)
		d1 = sort(d1)
		
		# merge
		d0.append('#')
		d1.append('#')
		p0, p1 = 0, 0
		for i in range(n):
			#print(f'd0: {d0}, d1: {d1}')
			if choose_min(d0[p0], d1[p1]) == 0:
				res.append(d0[p0])
				p0 += 1
			else:
				res.append(d1[p1])
				p1 += 1
		
		return res
		
	n = len(d)
	if n < m:
		print('Warning[prob5]: Books in shelf is not enough!')
	
	if n < 1:
		return []

	
	d_dif = [(i, abs(d[i] - a)) for i in range(n)]
	if d_dif:
		d_dif_sorted = sort(d_dif) 	
	
	result = []
	for i in range(min(m, n)):
		result.append(d_dif_sorted[i][0])

	return sort(result)


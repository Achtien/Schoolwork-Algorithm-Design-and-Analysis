def select_books(d, a, m):
	'''
	Paratemter:
		d: the difficulty indices of the books with shelf order.
		a: the student's reading ability.
		m: the number of books the student must select.

	Return:
		result: a list contains indices of the selectd books.
	'''
	def select(dif, s):
		n = len(dif)
		m = len(s)
		
		if m == 1:
			res = s[0]
			for i in range(n):
				if dif[i][1] < res[1]: res = dif[i]
			return [res]

		# divide
		s0 = s[:m//2]
		s1 = s[m//2:]
		dif0 = dif[:n//2]
		dif1 = dif[n//2:]

		# conquer and merge
		return select(dif0, s0) + select(dif1, s1)

	n = len(d)
	if m >= n:
		return list(range(n))

	d_dif = []
	for i in range(n):
		d_dif.append((i, abs(d[i]-a)))	

	s = []
	for i in range(m):
		s.append((-1, float('inf')))

	return [book[0] for book in select(d_dif, s)]

if __name__ == '__main__':
	print(select_books([18,11,17,4,8,6,10,13,10], 10, 3))

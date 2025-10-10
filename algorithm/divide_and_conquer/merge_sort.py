def choose_min(n0, n1):
	'''
	(auxiliary function)
	Description:
		Get two numbers, return the order number of the smaller
		one. '#' is supposed to be the largest number.

	Parameters:
		a, b: num

	Return:
		0: n0 is the smaller one.
		1: n1 is the smaller one.
	'''
	try:
		if n0 == '#':
			return 1
		elif n1 == '#':
			return 0
		elif n0 <= n1:
			return 0
		else:
			return 1
	except Exception as e:
		raise e

def merge_sort(ls, reverse=False):
	'''
	Parameters:
		ls: the list
		reverse=False: choose True if need decreasing order.

	Return:
		res: the sorted list
	'''
	n = len(ls)
	if n == 1:
		return ls
	
	# divide
	ls0 = ls[:n//2]
	ls1 = ls[n//2:]

	# conquar
	ls0 = merge_sort(ls0)
	ls1 = merge_sort(ls1)

	# merge
	ls0.append('#')
	ls1.append('#')
	res, p0, p1 = [], 0, 0
	for i in range(n):
		if choose_min(ls0[p0], ls1[p1]):
			res.append(ls1[p1])
			p1 += 1
		else:
			res.append(ls0[p0])
			p0 += 1
			
	if reverse:
		res_reverse = []
		for i in range(n):
			res_reverse.append(res[n-1 - i])
		res = res_reverse
	
	return res


if __name__ == '__main__':
	# test
#	print(merge_sort([4,2,3,9]))
	assert merge_sort([4,2,3,9]) == [2,3,4,9]
	assert merge_sort([4,2,3]) == [2,3,4]
	assert merge_sort([8,4,3,2,5]) == [2,3,4,5,8]
	assert merge_sort([4,3,2,7,5,3]) == [2,3,3,4,5,7]
	assert merge_sort([5,3,8],reverse=True) == [8,5,3]	
	assert merge_sort([1.6, 3.9, 10.8, 3, -5, 90]) == [-5, 1.6, 3, 3.9, 10.8, 90]

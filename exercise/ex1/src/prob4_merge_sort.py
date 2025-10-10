def choose_min(n0, n1):
	'''
	(auxiliary function)
	Description:
		Get two numbers, return the order number of the smaller
		one. '#' is supposed to be the largest number.

	Parameters:
		n1, n2: num

	Return:
		0: n0 is the smaller one.
		1: n1 is the smaller one.
	'''
	try:
		if n0 == '#':
			return 1
		elif n1 == '#':
			return 0
		elif n0[1] <= n1[1]:
			return 0
		else:
			return 1
	except Exception as e:
		raise e

def merge_sorted(ls, reverse=False):
	'''
	PARAMETERS:
	ls: the list
	reverse=False: choose True if need decreasing order

	RETURN:
	list -- the sorted list
	'''
	n = len(ls)
	if n == 1:
		return ls
	elif n == 0:
		return []
	
	# divide and conquer
	ls1 = ls[:n//2]
	ls2 = ls[n//2:]

	ls1 = merge_sorted(ls1)
	ls2 = merge_sorted(ls2)

	# merge
	ls1.append('#')
	ls2.append('#')
	res, p1, p2 = [], 0, 0
	for i in range(n):
		if choose_min(ls1[p1], ls2[p2]):
			res.append(ls2[p2])
			p2 += 1
		else:
			res.append(ls1[p1])
			p1 += 1
			
	if reverse:
		res_reverse = []
		for i in range(n):
			res_reverse.append(res[n-1 - i])
		res = res_reverse
	
	return res


if __name__ == '__main__':
	pass
#	print(merge_sorted([(0,2),(1,3),(2,5),(3,0),(4,30),(5,20)]))
#	print(merge_sorted([]))
	# test
#	assert order_merge_sorted([4,2,3,9]) == [(1,2),(2,3),(0,4),(3,9)]
#	assert merge_sorted([4,2,3]) == [2,3,4]
#	assert merge_sorted([8,4,3,2,5]) == [2,3,4,5,8]
#	assert merge_sorted([4,3,2,7,5,3]) == [2,3,3,4,5,7]
#	assert merge_sorted([5,3,8],reverse=True) == [8,5,3]	
#	assert merge_sorted([1.6, 3.9, 10.8, 3, -5, 90]) == [-5, 1.6, 3, 3.9, 10.8, 90]

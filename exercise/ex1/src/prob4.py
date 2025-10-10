from prob4_merge_sort import merge_sorted

def max_rev(k, profit1, profit2):
	'''

	'''
	try:
		if len(profit1) != len(profit2):
			return 0
		elif k > len(profit1):
			return sum(profit1)
		elif k <= 0:
			return sum(profit2)

		profit_dif = []
		for i in range(len(profit1)):
			profit_dif.append((i, profit1[i]-profit2[i]))
		profit_dif_sorted = merge_sorted(profit_dif, reverse=True)

		A_rev = 0
		assign = {}
		profit2_cp = profit2[:]
		for i in range(k):
			index = profit_dif_sorted[i][0]
			A_rev += profit1[index]
			assign.update({index:'A'})

			# mark the assigned jobs
			profit2_cp[index] = '#'

		B_rev = 0
		for i in range(len(profit1)):
			if profit2_cp[i] == '#':
				pass
			else:
				B_rev += profit2[i]
				assign.update({i:'B'})

		return A_rev+B_rev
	
	except Exception as e:
		print(f"Error: {e}")

if __name__ == '__main__':
	pass
	print(max_rev(2,[2,3,5,0,30,20],[4,1,1,2,100,100]))

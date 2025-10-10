def count_inversion(ini, tar):
	n = len(ini)
	ini = ini[:]
	tar = tar[:]

	ini_f = []
	tar_f = []
	for i in range(n):
		ini_f.append((i, ini[i]))
		tar_f.append((i, tar[i]))
	
	ini_f_s = sorted(ini_f, key=lambda x: x[1])
	tar_f_s = sorted(tar_f, key=lambda x: x[1])
	
	

	def find_position(num, a):
		n = len(a)
		left = 0
		right = n-1
		while left < right:
			mid = (left + right) // 2
			if a[mid] <= num:
				if a[mid+1] > num: return mid
				left = mid
			else:
				right = mid
		return -1

	# find initial order to target
	init_order = []
	target_sorted_min = [e[1] for e in ini_f]
	for e in tar_f:
		p = find_position(e[1], target_sorted_min)
		init_order.append(init_sorted[p][0])
	
	
	# calculate minimum operations.
	count = 0
	taken = []
	for i in range(n):
		take = init_order[i]
		p = find_position(init_order[i], taken)
		taken = taken[:p] + [take] + taken[p:]
		count += take - (p+1)

	return count

if __name__ == '__main__':
	pass
	#print(min_operations([3,2,1,4,5,6],[5,6,3,2,1,4]))

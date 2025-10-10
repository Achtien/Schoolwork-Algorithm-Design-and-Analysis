def min_operations(init, target):
	'''

	'''

	# check size
	try:
		if len(init) != len(target) or len(init) % 2 == 1 or len(init) < 4:
			return print("ERROR: Invalid size.")
	except Exception as e:
		return print(f"ERROR: {e}")

	n = len(init)//2
	init = init[:]	
	target = target[:]

	# initialize lists: [(initial_index, numbrow_0, num_row_1)]
	init_origin = []
	target_origin = []
	for i in range(n):
		init_origin.append((i, init[i], init[n+i]))
		target_origin.append((i, target[i], target[n+i]))
	
	#print(f'init_origin: {init_origin}\ntarget_origin: {target_origin}')

	init_sorted = sorted(init_origin, key = lambda x: min(x[1],x[2]))
	target_sorted = sorted(target_origin, key = lambda x: min(x[1],x[2]))
	
	#print(f'init_sorted: {init_sorted}\ntarget_sorted: {target_sorted}')

	# check if two lists match.
	for i in range(n):
		init_i = (min(init_sorted[i][1], init_sorted[i][2]), max(init_sorted[i][1], init_sorted[i][2]))
		target_i = (min(target_sorted[i][1], target_sorted[i][2]), max(target_sorted[i][1], target_sorted[i][2]))

		if init_i == target_i: 
			pass
		else:
			#print(f'not match')
			return print("ERROR: Numbers not match.")

	# check if it's possible to transform. If not, return -1
	for i in range(n):
		is_odd_init_i = init_sorted[i][0] % 2
		is_odd_target_i = target_sorted[i][0] % 2
		init_i = (init_sorted[i][1], init_sorted[i][2])
		target_i = (target_sorted[i][1], target_sorted[i][2])

		if is_odd_init_i == is_odd_target_i:
			if init_i == target_i:
				pass
			else:
				#print(f'in if, i = {i}')
				#print(is_odd_init_i, is_odd_target_i)
				return -1
		else:
			if init_i[1] == target_i[0] and init_i[0] == target_i[1]:
				pass
			else:
				#print(f'in else, i = {i}')
				return -1
	
	# calculate minimum operations.
	count = 0
	for i in range(n):
		dif = init_sorted[i][0] - target_sorted[i][0] > 0
		if dif > 0:
			count += dif

	return count

if __name__ == '__main__':
	pass
	#print(min_operations([3,2,1,4,5,6],[5,6,3,2,1,4]))

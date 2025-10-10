def find_p(num, a):
	n = len(a)
	left = 0
	right = n-1
	while left < right:
		print(f'left: {left}, right: {right}')
		mid = (left+right)//2
		if a[mid] <= num:
			if a[mid+1] > num: return mid
			left = mid
		else:
			right = mid
	return -1

if __name__ == '__main__':
	print(find_p(11,[]))

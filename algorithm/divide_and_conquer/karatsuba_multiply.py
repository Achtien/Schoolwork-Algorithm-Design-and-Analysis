def karatsuba_multiply(a, b):
	'''
	Multiply two decimal numbers with divide and conquer(karatsuba algorithm). 
	a * b 
	= (a0 * 10^(m/2) + a1)(b0 * 10^(m/2) + b1) = 
	= a0*b0*10^m + a1*b1 + 10^(m/2)((a0+a1)*(b0+b1) - a0*b0 - a1*b1)
	
	p1 = a0 * b0
	p2 = a1 * b1
	p3 = (a0+a1) * (b0+b1)

	a * b
	= 10^m * p1 + p2 + 10^(m/2) * (p3 - p1 - p2)


	Args:
		a: addend natural integer
		b: addend natural integer

	return:
		res: a + b
	'''
	m = max(len(str(a)), len(str(b)))
	if m == 1:
		return a*b
	round_m = 10**(m//2)
	
	# divide a, b to half(divide)
	a0 = a // round_m
	a1 = a - a0*round_m
	b0 = b // round_m
	b1 = b - b0*round_m

	# call kara for each four multiply(conquer)
	p1 = karatsuba_multiply(a0, b0)
	p2 = karatsuba_multiply(a1, b1)
	p3 = karatsuba_multiply(a0+a1, b0+b1)
	
	# shift and add them together(merge)
	res = round_m**2 * p1 + p2 + round_m * (p3 - p1 - p2)
	return res

if __name__ == '__main__':
	res1 = karatsuba_multiply(1234, 5678)
	print(f'1234 * 5678 = {res1} (7006652)')
	'''
	Debug Log:
		error:
			infinite recursion.

		modify: in m = max(equ1, equ2), equ1 = len(str(a)) not a // 10, as well equ2.

		error:
			infinite recursion.

		test:
			print(m) before return a*b, infinite print, m=1 or m=2.
			
		test:
			print(a, b, a0, b0, a1, b1) after b1 = b - b0

		modify:
			in divede, a1 = a - a0 * round_m not a1 = a - a0, b as well.

		Done.
	'''


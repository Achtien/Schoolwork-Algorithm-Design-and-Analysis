

class TotalCombatPower(object):
	"""

	"""
	def __init__(self,original_nums):
		try:
			self.original_nums = tuple(original_nums)
			self.nums = sorted(original_nums, reverse=True)
			self.sum = sum(self.nums)
			self.max_tcp, self.members = self.find_max_tcp()
			print(f'Total Combat Power: {self.max_tcp}\nmembers: {self.members}')
		except Exception as e:
			print(f'Max_TCP error: {e}')
	
	def find_max_tcp(self):
		sum_low = self.sum
		i = 0
		while i < len(self.nums) - 2:
			if self.nums[i] >= sum_low - self.nums[i]:
				sum_low -= self.nums[i]	
				i += 1
				pass
			else:
				return round(sum_low, 3), self.nums[i:]
		return 0, []



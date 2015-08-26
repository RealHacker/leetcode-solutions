class Solution(object):
	def maxProduct(self, nums):
		products= {}
		_max = None
		for i in range(len(nums)):
			for j in range(0,len(nums)-i):
				if i == 0:
					products[(j, j)] = nums[j]
				else:
					products[(j, j+i)] = products[(j, j+i-1)]* nums[j+i]
		if _max is None: 
			_max = products[(j, j+i)]
		elif products[(j, j+i)]>_max:
			_max = products[(j, j+i)]
		return _max
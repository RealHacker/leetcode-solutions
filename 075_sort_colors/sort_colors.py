class Solution:

    # @param {integer[]} nums

    # @return {void} Do not return anything, modify nums in-place instead.

    def sortColors(self, nums):
	temp = [1 for i in range(len(nums))]
	red = 0
	blue = len(nums)-1
	for i in range(len(nums)/2):
		num = nums[i]	
		if num == 0:
			temp[red]=0
			red = red+1
		if num == 2:
			temp[blue] = 2
			blue -= 1
	nums = temp

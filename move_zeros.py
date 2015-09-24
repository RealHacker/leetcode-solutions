class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1
        for i in range(len(nums)):
            num = nums[i]
            if num:
                if zero >= 0:
                    nums[i], nums[zero] = nums[zero], nums[i]
                    zero += 1
            else:
                if zero<0:
                    zero = i
                

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        split_at = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]<nums[i]:
                split_at = i
                break
        if split_at < 0:
            nums.reverse()
        else:
            for i in range(len(nums)-1, split_at-1, -1):
                if nums[i]>nums[split_at-1]:
                    nums[i], nums[split_at-1] = nums[split_at-1], nums[i]
                    break
            nums[split_at:] = sorted(nums[split_at:])
            

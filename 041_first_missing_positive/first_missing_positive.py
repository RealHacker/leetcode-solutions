class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        while i<l:
            if nums[i]>0 and nums[i]<= l and nums[i]!=i+1:
                j = nums[i]-1
                if nums[j]!=j+1:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    i+=1
            else:
                i+=1
        for i, num in enumerate(nums):
            if num!=i+1:
                return i+1
        return l+1

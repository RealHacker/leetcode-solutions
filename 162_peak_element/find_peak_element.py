class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        l = len(nums)
        left = 0 
        right = l-1
        i = 0
        while True:
            i = (left+right)/2
            if i>0 and nums[i-1]>nums[i]:
                right = i-1
                continue
            if i<l-1 and nums[i]<nums[i+1]:
                left = i+1
                continue
            break
        return i

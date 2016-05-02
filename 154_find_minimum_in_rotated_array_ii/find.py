class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None
        if len(nums)==1: return nums[0]
        if nums[0]<nums[-1]: return nums[0]
        if nums[0]==nums[-1]:
            # remove all duplicates at the end, and all but one duplicates at the beginning
            i=0
            while i<len(nums) and nums[i]==nums[0]:
                i+=1
            i-=1
            j = len(nums)-1
            while nums[j]==nums[0] and j>i:
                j-=1
            j+=1
            return self.findMin(nums[i:j])
        else:
            i, j = 0, len(nums)-1
            while i!=j:
                pos = (i+j)/2
                if nums[pos]>=nums[0]:
                    i = pos+1
                else:
                    j = pos
            return nums[i]
        

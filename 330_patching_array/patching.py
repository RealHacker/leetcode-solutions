class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        
        reached = 0
        patched = 0
        i = 0
        
        while True:
            if i<len(nums) and nums[i]<=reached+1:
                reached += nums[i]
                i+=1
            else:
                patched += 1
                reached += reached+1
            if reached >= n:
                break
        return patched
            

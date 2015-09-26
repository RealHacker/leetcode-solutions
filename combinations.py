class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = list(range(1, n+1))
        return self.recurse(nums,k)
        
    def recurse(self, nums, k):
        if k>len(nums):
            return []
        if k==len(nums):
            return [nums[:]]
        if k==1:
            return [[num] for num in nums]
        sub = self.recurse(nums[1:], k-1)
        result = [[nums[0]]+item for item in sub]
        result += self.recurse(nums[1:], k)
        return result

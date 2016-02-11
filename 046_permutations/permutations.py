class Solution(object):
    def permute(self, nums):
        return self.sub(nums)
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

    def sub(self, nums):
        if len(nums) == 0: return [[]]
        if len(nums) == 1: return [nums]
        pattern = self.sub(nums[1:])
        c = []
        for i in xrange(len(nums)):
            for p in pattern:
                c.append(p[:i] + [nums[0]] + p[i:])
        return c

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected = (len(nums)+1)*len(nums)/2
        return expected-sum(nums)

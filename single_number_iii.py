class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor = xor^num
        lastbit = xor&(-xor)
        filtered = filter(lambda x: x&lastbit, nums)
        n = 0
        for num in filtered:
            n = n ^ num
        return (n, n^xor)
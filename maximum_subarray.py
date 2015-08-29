class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = None
        sum = 0
        current = None
        for i in nums:
            sum = sum + i
            if maxsum is None or sum > maxsum:
                maxsum = sum
            if sum < 0:
                sum = 0
                
            if i>=0:
                if current is None:
                    current = 0
                current = current + i
            elif current is not None:
                if maxsum is None or current >maxsum:
                    maxsum = current
                current = 0
        return maxsum

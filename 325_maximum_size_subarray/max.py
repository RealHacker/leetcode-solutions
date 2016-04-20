from collections import defaultdict
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = defaultdict(list)
        sum = 0
        result = 0
        for i,num in enumerate(nums):
            sums[sum].append(i)
            sum += num
            if sum-k in sums:
                result = max(result,i+1-sums[sum-k][0])

        return result
        

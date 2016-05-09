class Solution(object):
        def maxCoins(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums = [1] + nums + [1] # build the complete array 
            n = len(nums)
            dp = [[0] * n for _ in xrange(n)]

            for gap in xrange(2, n):
                for i in xrange(n-gap):
                    j = i + gap
                    for k in xrange(i+1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
            return dp[0][n-1]

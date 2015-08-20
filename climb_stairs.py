class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        ways = {}
        def getways(m):
            if m==n-1:
                return 1
            elif m==n-2:
                return 2
            if m in ways:
                return ways[m]
            else:
                ways[m] = getways(m+1)+getways(m+2)
                return ways[m]
        return getways(0)
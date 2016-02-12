class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
    	dp = {}
    	def canReach(i):
    		print i
    		last = len(nums)-1
    		if i>=last:
    			return True
    		if i in dp:
    			return dp[i]
    		for j in range(1, nums[i]+1):
    			if canReach(i+j):
    				dp[i] = True
    				return True
    		dp[i]=False
    		return False
    	return canReach(0)

print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])

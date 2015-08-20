class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
    	max_reach = 0
    	for i, m in enumerate(nums):
    		if i>max_reach:
    			return False
    		max_reach = max(max_reach, i+nums[i])
    	return max_reach>=len(nums)-1

print Solution().canJump([2,3,1,1,4])
print Solution().canJump([3,2,1,0,4])

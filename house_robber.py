class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.memo = {} # idx -> max robbery
        def get_max_rob(idx):
            if idx in self.memo:
                return self.memo[idx]
            if idx >= len(nums):
                return 0
            
            if idx == len(nums)-1:
                _max = nums[idx]
            elif idx == len(nums)-2:
                _max = max(nums[idx], nums[idx+1])
            else:
                _max = max(nums[idx]+get_max_rob(idx+2), get_max_rob(idx+1))
            
            self.memo[idx]= _max
            return _max
        
        return get_max_rob(0)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.memo = {} # idx -> max robbery
        def get_max_rob(idx, droplast=False):
            if (idx, droplast) in self.memo:
                return self.memo[idx, droplast]
            if idx >= len(nums):
                return 0
            
            if idx == len(nums)-1:
                if droplast:
                    _max = 0
                else:
                    _max = nums[idx]
            elif idx == len(nums)-2:
                if droplast:
                    _max = nums[idx]
                else:
                    _max = max(nums[idx], nums[idx+1])
            else:
                _max = max(nums[idx]+get_max_rob(idx+2, droplast), get_max_rob(idx+1, droplast))
            
            self.memo[idx, droplast]= _max
            return _max
        return max(nums[0]+ get_max_rob(2, True), get_max_rob(1))

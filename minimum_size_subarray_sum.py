class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # sliding window 
        left = 0
        _min = sys.maxint
        _sum = 0
        for i in range(len(nums)):
            _sum = _sum+nums[i]
            if _sum<s: continue
            while _sum >= s:
                _sum -= nums[left]
                left +=1
            left -=1
            _sum+=nums[left]
            
            if i-left+1<_min:
                _min = i-left+1
        if _min == sys.maxint:
            return 0
        return _min
        

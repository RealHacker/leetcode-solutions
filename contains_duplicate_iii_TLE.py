class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k==0:
            return False
            
        if t>=max(nums)-min(nums):
            return True
        if k>=len(nums):
            _mingap = sys.maxint
            _nums = sorted(nums)
            for i in range(len(nums)-1):
                gap = _nums[i+1]-_nums[i]
                if gap<_mingap:
                    _mingap = gap
            return _mingap<=t
            

        _min = min(k, len(nums))
        window = []
        for i in range(_min):
            val = nums[i]
            for v in window:
                if v-t<=val<=v+t: 
                    return True
            window.append(val)
                
        for n in range(_min, len(nums)):
            val = nums[n]
            del window[0]
            for v in window:
                if v-t<=val<=v+t: 
                    return True
            window.append(val)
        return False
            

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        window = []
        def check_distance_t(i):
            if i>0 and abs(window[i]-window[i-1])<=t:
                return True
            if i<len(window)-1 and abs(window[i]-window[i+1])<=t:
                return True
            return False
            
        
        start = min(k+1, len(nums))
        for i in range(start):
            idx = bisect.bisect_left(window, nums[i])
            window.insert(idx, nums[i])
            if check_distance_t(idx):
                return True
        end = 0
        
        while start<len(nums):
            idx = bisect.bisect_left(window, nums[end])
            del window[idx]
            idx = bisect.bisect_left(window, nums[start])
            window.insert(idx, nums[start])
            if check_distance_t(idx):
                return True
            start += 1
            end += 1
        
        return False
            
            

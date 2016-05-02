import sys
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        self.nums = nums
        self.max = - sys.maxint
        self.map = {}
        for i in range(len(nums)-1, -1, -1):
            self.maxStartFrom(i)
        return self.max
        
    def maxStartFrom(self, i):
        if i==len(self.nums)-1:
            if self.nums[i]>self.max:
                self.max = self.nums[i]
            if self.nums[i]==0:
                self.map[i] =  (0, 0)
            elif self.nums[i]>0:
                self.map[i] =(self.nums[i], None)
            else:
                self.map[i] = (None, self.nums[i])
        else:
            _max, _min = self.map[i+1]
            if self.nums[i]==0:
                _max_, _min_ = (0, 0)
            elif self.nums[i]>0:
                if _max is None:
                    _max_ = self.nums[i]
                else:
                    _max_ = max(self.nums[i], self.nums[i]*_max)
                _min_ = self.nums[i]*_min if _min is not None else None
            else:
                if _min is None:
                    _max_ = None
                else:
                    _max_ = self.nums[i]*_min
                if _max is None:
                    _min_ = self.nums[i]
                else:
                    _min_ = min(self.nums[i], self.nums[i]*_max)
            if _max_ is not None and _max_>self.max:
                self.max = _max_
            elif _min_ is not None and _min_>self.max:
                self.max = _min_
            self.map[i] = _max_, _min_
            
                
                
                

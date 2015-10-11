class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==1:
            return 0
        candidates = [0]
        step = 0
        while True:
            # print candidates
            step += 1
            _min = max(candidates)+1
            _max = _min
            for c in candidates:
                c = c + nums[c]
                if c > _max:
                    _max = c
            if _max>=len(nums)-1:
                return step
            candidates = range(_min, _max+1)

                
        

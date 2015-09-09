class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        _min, _max = min(nums), max(nums)
        if _min==_max:
            return 0
        bucket_size = (_max-_min)/len(nums)+1
        
        buckets = [None for i in range(len(nums))]
        # put in buckets
        for num in nums:
            index = (num-_min)/bucket_size
            if not buckets[index]:
                buckets[index] = [num, num]
            else:
                if num<buckets[index][0]:
                    buckets[index][0]=num
                elif num>buckets[index][1]:
                    buckets[index][1] = num
        maxgap = buckets[0][1]- buckets[0][0]
        _last = buckets[0][1]
        for i in range(1, len(buckets)):
            if not buckets[i]:
                continue
            newgap = buckets[i][0]-_last
            if newgap>maxgap:
                maxgap = newgap
            _last = buckets[i][1]
            
        return maxgap
                

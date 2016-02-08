from collections import defaultdict
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if len(nums)<2:
            return len(nums)
        d = defaultdict(int)
        p = {}
        idx = 0
        while idx<len(nums):
            num = nums[idx]
            if d[num]<2:
                d[num]+=1
                idx += 1
            else:
                del nums[idx]
        cnt = 0
        for key in d:
            cnt += d[key]
        
        return cnt


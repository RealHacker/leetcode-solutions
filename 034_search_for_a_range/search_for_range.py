import bisect
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        if l >= len(nums) or nums[l]!=target:
            l = -1
        if r == 0 or nums[r-1] != target:
            r = -1
        else:
            r = r-1
        return [l, r]
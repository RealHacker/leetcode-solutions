from collections import Counter
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        c = Counter(nums[:k])
        for val in c.values():
            if val>1:
                return True
        start = 0
        end = k
        while end < len(nums):
            if c[nums[end]]>0:
                return True
            c[nums[start]]-=1
            c[nums[end]]+=1
            start += 1
            end += 1
        return False
import bisect
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        end = len(nums1)-1
        while end>=m:
            del nums1[end]
            end -= 1
        
        for j in range(n):
            num = nums2[j]
            pos = bisect.bisect_left(nums1, num)
            nums1.insert(pos, num)
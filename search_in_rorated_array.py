import bisect
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if nums[0]<nums[-1]:
            min_index = 0
        else:
            first = nums[0]
            l = 0
            r = len(nums)-1
            while l<r:
                j = (l+r)/2
                if nums[j] < first:
                    r = j
                else:
                    l = j+1
            min_index = r
        sorted_nums = nums[min_index:] + nums[:min_index]
        print sorted_nums, min_index
        pos = bisect.bisect_left(sorted_nums, target)
        if pos<len(nums) and sorted_nums[pos]==target:
            return (min_index+pos)%len(nums)
        else:
            return -1

print Solution().search([3,0,1], 0)

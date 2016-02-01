import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        assert(len(nums)>=3)
        nums = sorted(nums)
        diff = sys.maxint
        number = None
        for i in range(len(nums)-2):
            first = nums[i]
            head = i+1
            tail = len(nums)-1
            while head<tail:
                s = first + nums[head]+ nums[tail]
                if abs(s-target)<diff:
                    diff = abs(s-target)
                    number = s
                if s<target:
                    head += 1
                elif s>target:
                    tail -= 1
                else:
                    return target
        return number
        

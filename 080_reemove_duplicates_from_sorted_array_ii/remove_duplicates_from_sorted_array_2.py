class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i]!=nums[i-1]:
                c = 1
            else:
                c+=1
                if c >=3:
                    c-=1
                    del nums[i]
        return len(nums)

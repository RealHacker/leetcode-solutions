class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return 0
        nums.sort()
        
        count = 0
        numslen = len(nums)
        for i in range(numslen-2):
            j = i+1
            k = numslen-1
            while j<k:
                while j<k and nums[i] + nums[j]+ nums[k]>=target:
                    k -= 1
                count += k-j
                j+=1
        return count

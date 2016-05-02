class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]<nums[-1]:
            return nums[0]
        i, j = 0, len(nums)-1
        while True:
            if i>=j:
                break
            idx = (i+j)/2
            if nums[idx]>nums[0]:
                i = idx+1
            elif nums[idx]<nums[0]:
                j = idx
            elif nums[idx]>nums[-1]:
                i = idx+1
            else:
                j = idx
                
        if nums[i]<nums[j]:
            ret = i
        else:
            ret = j
        if nums[ret]<=nums[0]:
            return nums[ret]
        else:
            while nums[ret]>nums[0]:
                ret +=1
            return nums[ret]
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while True:
            # partition
            p = start
            for i in range(start, end):
                if nums[i]>nums[end]:
                    nums[i], nums[p]= nums[p],nums[i]
                    p+=1
            nums[end], nums[p] = nums[p], nums[end]
            
            if p==k-1:
                return nums[p]
            elif p<k-1:
                start = p+1
            else:
                end = p-1
        
                

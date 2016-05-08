class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        q = []
        for i, num in enumerate(nums):
            while q and nums[q[0]]<num: 
                q.pop(0)
            q.insert(0, i)
            if i>=k-1:
                if i>=k and q[-1]==i-k:
                    q.pop()
                result.append(nums[q[-1]])
        return result
        

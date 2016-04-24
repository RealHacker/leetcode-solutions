class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frontier = []
        for num in nums:
            if not frontier or num>frontier[-1]:
                frontier.append(num)
            else:
                idx = bisect.bisect_left(frontier, num)
                frontier[idx] = num
        return len(frontier)
        
            

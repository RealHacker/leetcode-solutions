class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = set()
        for i in range(len(nums)+1):
            self.getCombi(nums, i,[])
            
        return list(self.result)
        
    def getCombi(self, nums, i, temp):
        if i==0:
            self.result.add(tuple(sorted(temp)))
        elif not nums:
            return
        else:
            self.getCombi(nums[1:], i-1, temp+[nums[0]])
            self.getCombi(nums[1:], i, temp)

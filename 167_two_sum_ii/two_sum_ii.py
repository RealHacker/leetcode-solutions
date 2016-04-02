class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<2:return []
        start = 0
        end = len(numbers)-1
        
        while True:
            n = numbers[start]+numbers[end]
            if n==target:
                return [start+1, end+1]
            elif n<target:
                start+=1
            else:
                end-=1
            if start==end:
                return []
        

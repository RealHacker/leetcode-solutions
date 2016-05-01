class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        negatives = 0
        for i in range(32):
            mask = 1<<i
            temp = 0
            for num in nums:
                if num<0:
                    negatives += 1
                    num = -num
                temp += 1 if num&mask else 0
            temp = temp%3
            if temp:
                result |= mask
        if negatives%3:
            return -result
        else:
            return result
            
            

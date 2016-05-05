class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        base = 26
        digits = 1
        while n>base:
            n -= base
            base = base*26
            digits += 1
        
        n = n-1
        for i in range(digits):
            m = n%26
            result = chr(ord('A')+m) + result
            n = n/26
        
        return result
        
                
        

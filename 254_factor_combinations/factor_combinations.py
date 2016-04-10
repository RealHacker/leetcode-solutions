import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.memo = {}
        return self.recurse(n)
        
    def recurse(self, n):
        if n in self.memo:
            return self.memo[n]
        result = []
        sqrtn = int(math.sqrt(n))+1
        for i in range(2, sqrtn):
            if n%i==0:
                result.append([i, n/i])
                sub = self.recurse(n/i)
                for lst in sub:
                    if lst[0]>=i:
                        result.append([i]+lst)
        self.memo[n] = result
        return result
                

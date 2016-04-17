class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        self.memo = {}
        return self.recurse(n, k)
        
    def recurse(self, n, k):
        if n==0: return 0
        if n==1: return k
        if n==2: return k*k
        if n not in self.memo:
            self.memo[n] = self.recurse(n-1,k)*(k-1)+self.recurse(n-2,k)*(k-1)
        return self.memo[n]
        
        
        
        
        

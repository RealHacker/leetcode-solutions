class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 1
        if n==1:return 1
        if n==2:return 2
        if n==3:return 5
        self.map = {0:1, 1:1, 2:2, 3:5}
        return self._getnum(n)
        
    def _getnum(self, n):
        if n in self.map:
            return self.map[n]
        total = 0
        for i in range(n):
            left = self._getnum(i)
            right = self._getnum(n-i-1)
            total += left*right
        self.map[n] = total
        return total

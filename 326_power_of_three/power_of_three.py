class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        import math
        root = int(math.sqrt(n))
        i = 1
        while i<root:
            i*=3
        if i!=root:
            root = i/3
        if n%(root*root):
            return False
        return n/(root*root) in (1,3)

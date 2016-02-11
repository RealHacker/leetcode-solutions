class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        negative = False
        if n<0:
            n = -n
            negative = True
        m = self.myPow(x, n/2)
        result = m * m
        if n%2:
            result = result *x
        if negative:
            return 1.0/result
        else:
            return result

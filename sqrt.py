class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:return 0
        if x==1:return 1
        start = 1
        end = x
        last = -1
        while True:
            mid = (start+end)/2
            if mid==last:
                return mid
            if mid**2 == x:
                return mid
            elif mid**2<x:
                start = mid
            else:
                end = mid
            last = mid
        

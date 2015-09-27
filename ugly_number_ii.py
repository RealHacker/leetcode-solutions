class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        results = [1]
        
        i2, i3, i5 = 0,0,0
        while True:
            _min = min(results[i2]*2, results[i3]*3, results[i5]*5)
            results.append(_min)
            if len(results)==n:
                return results[-1]
            if _min == results[i2]*2:
                i2+=1
            if _min == results[i3]*3:
                i3+=1
            if _min == results[i5]*5:
                i5+=1
        

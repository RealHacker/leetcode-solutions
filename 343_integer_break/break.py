class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        _max = 0
        
        for i in range(2, n+1):
            splits = [n/i] * i
            if n%i:
                for j in range(n%i):
                    splits[j]+=1
            product = 1
            for split in splits:
                product *= split
            if product >= _max:
                _max = product
            else:
                break
        return _max

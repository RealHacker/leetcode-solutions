class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return 0
        seive = [1 for i in range(n)]
        seive[0]=0
        seive[1]=0
        i = 2
        while i*i<=n:
            if not seive[i]:
                i+=1
            else:
                j = i
                while i*j<n:
                    seive[i*j] = 0
                    j+=1
                i = i+1
        return sum(seive)

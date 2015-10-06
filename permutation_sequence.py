class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(m):
            if m==1:return 1
            return m*factorial(m-1)
        if n==1:
            return "1"
        units = [factorial(m) for m in range(n-1, 0, -1)]
        #print units
        i=0
        result = ""
        s = range(1,n+1)
        while k:
            m = k/units[i]
            k = k%units[i]
            if k:
                num = s[m]
            else:
                num = s[m-1]
            result += str(num)
            s.remove(num)
            # print result
            i+=1
        result += ''.join(map(str, sorted(list(s), reverse=True)))
        return result

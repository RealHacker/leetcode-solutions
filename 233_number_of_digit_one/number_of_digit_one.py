class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0: return 0
        def getNum(m):
            if m==0:
                return 0
            if m==1:
                return 1
            return getNum(m-1)*10+10**(m-1)
        k=1
        result = 0
        part = 0
        while n:
            m = n%10
            result += m*getNum(k-1)
            if m==1:
                result += part+1 
            elif m>1:
                result += 10**(k-1)
            part = part+m*(10**(k-1))
            n = n/10
            k+=1
        return result

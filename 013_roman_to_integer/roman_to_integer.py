class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = (('I',1),
            ('V',5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),)
        indice = {nums[i][0]: i for i in range(len(nums))}
        d = dict(nums)
        n = 0
        for i in range(len(s)):
            current = s[i].upper()
            if i<len(s)-1:
                next = s[i+1].upper()
                
                if indice[current]<indice[next]:
                    n -= d[current]
                else:
                    n += d[current]
            else:
                n+= d[current]
        return n

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==s[::-1]:return 0
        if len(s)==1: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        self.d = {}
        for i in range(0,len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if substr==substr[::-1]:
                    self.d[(i,j)]=0
        return self.recurse(0, len(s))

    def recurse(self, i, j):
        if (i, j) in self.d :
            return self.d[(i,j)]
        _min = j-i+1
        for k in range(i+1, j):
            if (i, k) in self.d and self.d[(i, k)]==0:
                newmin = 1+self.recurse(k, j)
                if newmin<_min:
                    _min = newmin
        self.d[(i,j)]=_min
        return _min

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.w1 = word1
        self.w2 = word2
        self.table = {}
        return self.recurse(0,0)
    
    def recurse(self, i1, i2):
        if (i1, i2) in self.table:
            return self.table[(i1, i2)]
        if i1==len(self.w1):
            result = len(self.w2)-i2
        elif i2==len(self.w2):
            result = len(self.w1)-i1
        elif self.w1[i1]==self.w2[i2]:
            result = self.recurse(i1+1, i2+1)
        else:
            # delete a char from w1
            d1 = self.recurse(i1+1, i2)
            d2 = self.recurse(i1, i2+1)
            d3 = self.recurse(i1+1, i2+1)
            result = min(d1, d2, d3)+1
        self.table[(i1, i2)]=result
        return result

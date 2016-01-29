from collections import defaultdict

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2) or set(s1)!=set(s2):
            return False
        if s1==s2:
            return True
        if not s1 and not s2:
            return True
        return self.recurse(s1, s2) or self.recurse(s1, s2[::-1])
            
    def recurse(self, s1, s2):
        d = defaultdict(int)
        breakpoints = []
        for i, c in enumerate(s1[:-1]):
            d[c]+=1
            c2 = s2[i]
            d[c2]-=1
            same = True
            for cc in d:
                if d[cc]!=0:
                    same=False
                    break
            if same:
                breakpoints.append(i)
        
        for b in breakpoints:
            if self.isScramble(s1[:b+1], s2[:b+1]) and self.isScramble(s1[b+1:], s2[b+1:]):
                return True
        return False
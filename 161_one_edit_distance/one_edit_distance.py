class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s)-len(t))>1:
            return False
        if len(s)==len(t):
            diff = 0
            for i in range(len(s)):
                if s[i]!=t[i]:
                    diff += 1
                    if diff>1: return False
            return diff==1
        if len(s)<len(t):
            s, t = t, s
        for i in range(len(t)):
            if s[i]!=t[i]:
                return s[i+1:]==t[i:]
        return True

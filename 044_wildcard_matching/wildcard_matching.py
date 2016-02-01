from collections import defaultdict

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print s, p
        if s and not p: return False
        
        # print s, p
        while s and p and p[0]!="*":
            if p[0]=="?" or p[0]==s[0]:
                p = p[1:]
                s = s[1:]
                print s, p
            else:
                return False

        if not p:
            return not s
        while s and p and p[-1]!="*":
            if p[-1]=="?" or p[-1]==s[-1]:
                p = p[:-1]
                s = s[:-1]
            else:
                return False
        # print s

        def find(seg, s):
            for i in range(len(s)-len(seg)+1):
                found = True
                for j in range(len(seg)):
                    if seg[j]=="?" or seg[j]==s[i+j]:
                        continue
                    else:
                        found=False
                        break
                if found:
                    return True, s[i+j+1:]
            return False, ""
                
            
        segments = filter(lambda s:s, p.split("*"))
        # print segments
        for segment in segments:
            found, s = find(segment, s)
            if not found:
                return False
        return True
                

        
import sys
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        stack = []
        tail = 0
        
        tdict = defaultdict(int)
        for c in t:
            tdict[c]+=1
        sdict = defaultdict(int)
        for c in s:
            sdict[c]+=1
            
        for c in tdict:
            if c not in sdict or sdict[c]<tdict[c]:
                return ""
            
        minw = sys.maxint
        mins = ""
        count = len(tdict)
        for i,c in enumerate(s):
            if c in tdict:
                tdict[c]-=1
                if tdict[c]==0:
                    count-=1

                if count==0:
                    # advance the tail
                    for j in range(tail, i):
                        if s[j] in tdict:
                            if tdict[s[j]]==0:
                                tail = j
                                break
                            tdict[s[j]]+=1
                    w = i-tail+1
                    if w<minw:
                        minw = w
                        mins = s[tail:i+1]
        return mins

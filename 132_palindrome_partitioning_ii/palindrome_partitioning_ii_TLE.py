class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==s[::-1]:return 0
        if len(s)==1: return 0
        d = set()
        for i in range(0,len(s)):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if substr==substr[::-1]:
                    d.add((i,j))
        print d
        q = [[0,len(s)]]
        while True:
            seq = q.pop(0) 
            curlen = len(seq)-2
            if (seq[-2],seq[-1]) in d:
                return curlen
            if seq[-2]<seq[-1]:
                for k in range(seq[-2]+1, seq[-1]):
                    if (seq[-2], k) in d:
                        newseq = seq[:-1]+[k, seq[-1]]
                        q.append(newseq)

from collections import defaultdict
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        # first they need the same composition
        counter = defaultdict(int)
        for c in s1+s2:
            counter[c]+=1
        for c in s3:
            counter[c]-=1
        for c in counter:
            if counter[c] != 0:
                return False
        self.memo = {}
        return self._isInterleave(s1, s2, s3)
    
    def _isInterleave(self, s1, s2, s3):
        if (s1, s2, s3) in self.memo:
            return self.memo[(s1, s2, s3)]
            
        if not s1:
            ret = (s2 == s3)
            self.memo[(s1, s2, s3)]=ret
            return ret
        if not s2:
            ret = (s1 == s3)
            self.memo[(s1, s2, s3)]=ret
            return ret
        
        ret = False
        if s3[0] == s1[0]:
            ret = ret or self._isInterleave(s1[1:], s2, s3[1:])
        if s3[0] == s2[0]:
            ret = ret or self._isInterleave(s1, s2[1:], s3[1:])
        self.memo[(s1, s2, s3)] = ret
        return ret

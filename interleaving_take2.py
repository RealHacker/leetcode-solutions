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
        if not self.computeIndexes(s1, s3):
            return False
        return self.consume(s1, s2, "", s3, len(s1))
    
    def computeIndexes(self, s1, s3):
        self.indexs = []
        s3 = s3[::-1]
        s1 = s1[::-1]
        l = len(s3)
        for c in s1:
            idx = -1 if not self.indexs else self.indexs[-1]
            idx = s3.find(c, idx+1)                
            if idx <0:
                return False
            self.indexs.append(idx)
            #print self.indexs
        self.indexs = [l-idx for idx in self.indexs]
        return True            
            
    
    def consume(self, s1, s2, front, end, l):
        if not s2.startswith(front):
            return False
        if not s1:
            if s2==front+end:
                return True
            else:
                return False
        else:
            c = s1[0]
            limit = self.indexs[l-1]
            idx = -1
            while True:
                idx = end.find(c, idx+1)
                if idx < 0 or idx>limit:
                    break
                
                if self.consume(s1[1:], s2, front+end[:idx], end[idx+1:], l-1):
                    return True
            return False
            
                
        

print Solution().isInterleave("aa", "ab", "aaba")
print Solution().isInterleave("cbaccccacbcaaaccccaacbccabba", "babbacacbaabbcccabcaca", "baabbacbacccacacbcabcaaabbaccccccccacabcbccabacaba")
print Solution().isInterleave("ab", "bc", "bbac")
print Solution().isInterleave("cacbbbaaabbacbbbbabbcaccccabaaacacbcaacababbaabbaccacbaabac", "cbcccabbbbaaacbaccbabaabbccbbbabacbaacccbbcaabaabbbcbcbab", "ccbcccacbabbbbbbaaaaabbaaccbabbbbacbcbcbaacccbacabbaccbaaabcacbbcabaabacbbcaacaccbbacaabababaabbbaccbbcacbbacabbaacb")

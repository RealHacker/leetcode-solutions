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
        
        for perm in self.pick_permutation([], len(s1), len(s2)):
            s = s1
            for i,pos in enumerate(perm):
                s = s[:pos+i]+s2[i]+s[pos+i:]
            if s==s3:
                return True
        return False
                
    def pick_permutation(self, current, m, n):
        if len(current)==n:
            yield current
        else:
            if not current:
                start = 0
            else:
                start = current[-1]
            for i in range(start, m+1):
                new_current = current[:]
                new_current.append(i)
                for perm in self.pick_permutation(new_current,m,n):
                    yield perm

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print Solution().isInterleave(s1, s2, s3)

s1 = "abaaacbacaab"
s2 = "bcccababccc"
s3 ="bcccabaaaaabccaccbacabb"
print Solution().isInterleave(s1, s2, s3)

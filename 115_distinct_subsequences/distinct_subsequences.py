import sys
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        self.memo = {}
        self.s = ""
        self.t = t
        for c in t:
            if c not in s:
                return 0

        for c in s:
            if c in t:
                self.s += c
        return self.countSubs(0,0)
        
    def countSubs(self, s, t):
        if (s, t) in self.memo:
            return self.memo[(s,t)]
        isSub = 0
        if self.s[s:] == self.t[t:] or not self.t[t:]:
            isSub = 1
        elif len(self.s[s:])<=len(self.t[t:]):
            isSub = 0
        elif self.s[s]==self.t[t]:
            isSub = self.countSubs(s+1, t+1)+self.countSubs(s+1, t)
        else:
            isSub = self.countSubs(s+1, t)
        self.memo[(s,t)]=isSub

        return self.memo[(s,t)]

s = "anacondastreetracecar";
t =  "contra"

print Solution().numDistinct(s, t)

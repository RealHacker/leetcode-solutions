class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        d1 = {}
        d2 = {}
        for i, c in enumerate(s):
            if c not in d1 and t[i] not in d2:
                d1[c] = t[i]
                d2[t[i]] = c
            else:
                if c in d1 and d1[c]!=t[i]:
                    return False
                if t[i] in d2 and d2[t[i]]!=c:
                    return False
                    
        return True
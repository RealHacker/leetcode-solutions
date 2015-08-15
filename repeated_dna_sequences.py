from collections import defaultdict
class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s)<=10:
            return []
        d = defaultdict(int)
        for i in range(len(s)-9):
            d[s[i:i+10]]+=1
        return [k for k in d if d[k]>1]

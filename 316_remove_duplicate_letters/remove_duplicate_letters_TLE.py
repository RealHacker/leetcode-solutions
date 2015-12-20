from collections import Counter
import copy
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.counter = Counter()
        chrs = set()
        for c in s:
            chrs.add(c)
            self.counter[c]+=1
        self.chrs = sorted(list(chrs))
        return self.recurse(s, self.chrs)
        
    def recurse(self, s, chrs):
        if not s:
            return ""
        c = s[0]
        if self.counter[c]==0:
            return self.recurse(s[1:], chrs)
        temp = self.counter[c]
        _chrs = copy.copy(chrs)
        self.counter[c] -= 1
        if self.counter[c]==0:
            _chrs.remove(c)
        if self.counter[c]==0 or c==_chrs[0]:
            result = c + self.recurse(s[1:], _chrs)
            self.counter[c]=temp
            return result
        else:
            candidate1 = self.recurse(s[1:], _chrs)
            self.counter[c] = 0
            candidate2 = c+self.recurse(s[1:], _chrs)
            result = min(candidate1, candidate2)
            self.counter[c] = temp
            return result

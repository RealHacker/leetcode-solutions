class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        all = set(s)
        chrs = sorted(list(all))
        for chr in chrs:
            idx = s.index(chr)
            if set(s[idx:])==all:
                s = s[idx:].replace(chr, '')
                return chr + self.removeDuplicateLetters(s)
        return ''
            

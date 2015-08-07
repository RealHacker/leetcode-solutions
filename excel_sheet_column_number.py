class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        i = 0
        for c in s:
            i = i*26 + ord(c)-ord('A')+1
        return i
            
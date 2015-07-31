class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if not s.strip():
            return 0
        return len(s.strip().split()[-1])
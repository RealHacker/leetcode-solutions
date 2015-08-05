from collections import Counter
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)

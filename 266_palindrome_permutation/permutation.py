from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(int)
        for c in s:
            d[c]+=1
        odd = 0
        for _, c in d.items():
            if c%2:
                odd+=1
        return len(s)%2==1 and odd==1 or odd==0

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s)==0:
            return [[]]
        if len(s)==1:
            return [[s]]
        result = []
        for i in range(1, len(s)+1):
            substr = s[:i]
            if substr==substr[::-1]:
                result.extend([[s[:i]]+item for item in self.partition(s[i:])])
        return result

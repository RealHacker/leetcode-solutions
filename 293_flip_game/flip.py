class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s)<2:
            return []
        results = []
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+':
                r = s[:i]+"--"+s[i+2:]
                results.append(r)
        return results

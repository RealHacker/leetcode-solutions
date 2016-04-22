class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = []
        for i in range(len(s)-1, -1,-1):
            rs.append(s[i])
        return ''.join(rs)

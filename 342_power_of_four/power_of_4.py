class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = bin(num)
        zeros = 0
        for i in range(3, len(s)):
            if s[i]!='0':
                return False
            zeros+=1
        return s[2]=='1' and zeros%2==0

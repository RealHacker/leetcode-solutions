class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        while num%5==0:
            num = num/5
        while num%3==0:
            num = num/3
        while num%2==0:
            num = num/2
        return num==1

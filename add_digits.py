class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # digital root = n - 9*floor(n-1/9)
        if num ==0:
            return 0
        import math
        return int(num - 9* math.floor((num-1)/9))

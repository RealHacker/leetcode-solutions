import string
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        start = 0
        negative = False
        if str[0]=="-":
            start = 1
            negative = True
        elif str[0]=="+":
            start = 1
        elif str[0] not in string.digits:
            return 0
        num = 0
        while start < len(str):
            if str[start] not in string.digits:
                break
            num = num *10 + int(str[start])
            start += 1
        if negative:
            num = -num
        if num > 2147483647:
            return 2147483647
        if num < -2147483648:
            return -2147483648
        return num

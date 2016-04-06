class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairs = {"1":"1","0":"0", "8":"8", "6":"9","9":"6"}
        if len(num)%2==0:
            half = len(num)/2
        else:
            half = len(num)/2+1
        for i in range(half):
            if num[i] not in pairs:
                return False
            if pairs[num[i]]!=num[len(num)-1-i]:
                return False
        return True
        

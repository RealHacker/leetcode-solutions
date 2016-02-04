class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x<0 or x%10==0:
            return False
        l = len(str(x))
        i = 1
        x1 = x2 = x
        while i<=l/2:
            left = x1/(10**(l-i))
            x1 = x1%(10**(l-i))
            right = x2%10
            x2 = x2/10
            if left != right:
                return False
            i+=1
        return True

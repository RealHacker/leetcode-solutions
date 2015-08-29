class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        carry = 1
        while i>=0:
            digits[i] = digits[i]+carry
            if digits[i]<10:
                carry = 0
                break
            else:
                digits[i] = digits[i]%10
                carry = 1
            i-=1
        if carry:
            digits.insert(0, 1)
        return digits

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        neg = False
        if x<0:
            neg =True
            x = -x
        print x
        reversed_int = int(''.join(reversed(str(x))))
        if reversed_int>(1<<31):
            reversed_int = 0
        if neg:
            return -reversed_int
        else:
            return reversed_int

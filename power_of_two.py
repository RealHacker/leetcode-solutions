class Solution:

    # @param {integer} n

    # @return {boolean}

    def isPowerOfTwo(self, n):

        if n==0:

            return False

        return '1' not in bin(n)[3:]

        

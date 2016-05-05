class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n<=0:
            return 0
        twos = 0
        fives = 0
        n2 = n
        while n2:
            n2 = n2/2
            twos += n2
        n5 = n
        while n5:
            n5 = n5/5
            fives += n5
        return min(twos, fives)

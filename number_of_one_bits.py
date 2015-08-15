class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        hamming_weight = 0
        while n:
            hamming_weight+= n&1
            n = n>>1
        return hamming_weight

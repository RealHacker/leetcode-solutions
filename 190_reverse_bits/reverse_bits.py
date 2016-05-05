class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binstr = bin(n)[2:]
        binstr = '0'*(32-len(binstr)) + binstr
        result = binstr[::-1]
        return int(result, base=2)
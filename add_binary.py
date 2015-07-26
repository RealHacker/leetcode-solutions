class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return bin(int(a, base=2)+int(b, base=2))[2:]

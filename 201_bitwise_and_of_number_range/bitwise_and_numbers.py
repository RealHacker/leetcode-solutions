class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        if m == 0 or n ==0:
            return 0
        b1 = bin(m)[2:]
        b2 = bin(n)[2:]
        
        if len(b1) != len(b2):
            s = "0"
        else:
            s = ""
            while True:
                if not b1:
                    break
                if b1[0] == b2[0]:
                    s = s + b1[0]
                else:
                    s = s + "0"*len(b1)
                    break
                    
                b1 = b1[1:]
                b2 = b2[1:]
        return int(s, base = 2)
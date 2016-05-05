class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s = ""
        
        while True:
            m = n/26
            k = n%26
            if k == 0:
                k = 26
                m = m - 1
            s = s + chr(ord('A')+k-1)
            if m==0:
                break
            n = m
        return s[::-1]


print Solution().convertToTitle(25)
print Solution().convertToTitle(33)
print Solution().convertToTitle(345233)

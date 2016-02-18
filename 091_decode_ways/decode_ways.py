class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
       if not s:
           return 0
       self.memo = {}
       return self.getCount(s, 0)
       
    def getCount(self, s, i):
        if i in self.memo:
            return self.memo[i]
        if not s:
            ret = 1
        elif len(s) ==1:
            if s!='0':
                ret = 1
            else:
                ret = 0
        else:
            if s[0]=='0':
                ret = 0
            else:
                ret = self.getCount(s[1:], i+1)
                if int(s[:2])<=26:
                    ret += self.getCount(s[2:], i+2)
        self.memo[i] = ret
        return ret

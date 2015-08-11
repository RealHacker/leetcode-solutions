class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        s = "1"
        for i in range(n-1):
            idx = 0
            news = ""
            for j in range(1,len(s)):
                if s[j] != s[j-1]:
                    news += str(j-idx)+s[idx]
                    idx = j
            news+=str(len(s)-idx)+s[idx]
            s = news
        return s

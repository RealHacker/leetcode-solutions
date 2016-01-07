class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        maxlen = 0
        self.longest = {}
        while i<len(s):
            if s[i]==")": 
                i = i+1
                continue
            else:
                l = self.find_longest(i, s)
                if l-i+1 > maxlen:
                    maxlen = l-i+1
                i = l+1
        return maxlen
    
    def find_longest(self, i, s):
        if i in self.longest:
            return self.longest[i]
        start = balance = i
        left = 0
        right = 0
        while True:
            if i>=len(s):
                self.longest[start] = balance
                return balance 
            if s[i]=="(":
                left +=1
            else:
                right += 1
            if left<right:
                self.longest[start] = balance
                return balance 
            if left==right:
                balance = i
            i=i+1
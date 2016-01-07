class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        maxlen = 0
        while i<len(s):
            if s[i]==")": 
                i = i+1
                continue
            else:
                l, f = self.find_longest(i, s)
                if l > maxlen:
                    maxlen = l
                i = f+1
        return maxlen
    
    def find_longest(self, i, s):
        left = 0
        right = 0
	fail = len(s)
        while True:
            if i>=len(s):
                return right*2, fail
            if s[i]=="(":
                left +=1
            else:
                right += 1
            if left<right:
		fail = i
                return left*2, fail
            i=i+1

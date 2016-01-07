class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxlen = 0
        start = -1
        for i, c in enumerate(s):
            if c=='(':
                if start>=0:
                    stack.append((c, start))
                    start = -1
                else:
                    stack.append((c, i))
            else:
                if stack and stack[-1][0]=="(":
                    length = i-stack[-1][1]+1
                    if length>maxlen:
                        maxlen = length
                    start = stack[-1][1]
                    stack.pop()
                else:
                    start = -1
                    stack.append((c, i))
        return maxlen

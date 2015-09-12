class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        m = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack or stack[-1]!=m[c]:
                    return False
                stack.pop()
        return not stack

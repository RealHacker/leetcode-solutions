class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generate("", n, n)
        return self.result
        
    def generate(self, current, left, right):
        if left>0:
            self.generate(current+"(", left-1, right)
        if left<right:
            self.generate(current+")", left, right-1)
        if right==0:
            self.result.append(current)
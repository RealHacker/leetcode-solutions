class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder)<2:
            return True
        root = preorder[0]
        breakpoint = -1
        for i in range(1, len(preorder)):
            if preorder[i]>root:
                if breakpoint<0:
                    breakpoint = i
            if preorder[i]<root and breakpoint>0:
                return False
        if breakpoint <0:
            breakpoint = len(preorder)
        return self.verifyPreorder(preorder[1:breakpoint]) and self.verifyPreorder(preorder[breakpoint:]) 

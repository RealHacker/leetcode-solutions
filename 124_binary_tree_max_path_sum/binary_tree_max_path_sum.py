# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest, maxlen = self.recurse(root)
        return maxlen
        
    def recurse(self, node):
        if not node:
            return 0, -sys.maxint
        l1, m1 = self.recurse(node.left)
        l2, m2 = self.recurse(node.right)
        l = max(l1, l2)+node.val if max(l1, l2)>0 else node.val
        m = max(m1, m2, l1+l2+node.val, node.val, l1+node.val, l2+node.val)
        return l, m
        

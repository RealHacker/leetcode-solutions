# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not hasattr(root, "max"):
            rob1 = self.recurse(root, True)
            rob2 = self.recurse(root, False)
            root.max = max(rob1, rob2)
        return root.max
        
    def recurse(self, root, robbed):
        if not root: return 0
        if robbed:
            return root.val+self.recurse(root.left, False)+self.recurse(root.right, False)
        else:
            return self.rob(root.left) + self.rob(root.right)
            

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.count = 0
        self.isUnival(root)
        return self.count
    
    def isUnival(self, root):
        left_same = not root.left or (self.isUnival(root.left) and root.left.val==root.val)
        right_same = not root.right or (self.isUnival(root.right) and root.right.val==root.val)
        if left_same and right_same:
            self.count += 1
            return True
        return False

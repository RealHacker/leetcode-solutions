# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        maximum = 1
        if root.left:
            maximum = max(maximum, self.maxDepth(root.left)+1)
        if root.right:
            maximum = max(maximum, self.maxDepth(root.right)+1)
        return maximum

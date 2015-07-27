# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root:
            return 0
        self.sum = 0
        self.visitNode(root, str(root.val))
        return self.sum
        
    def visitNode(self, node, v):
        if not node.left and not node.right:
            self.sum += int(v)
            
        if node.left:
            self.visitNode(node.left, v+str(node.left.val))
        if node.right:
            self.visitNode(node.right, v+str(node.right.val))
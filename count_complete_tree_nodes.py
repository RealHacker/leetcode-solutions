# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        def getDepth(node):
            if not node:
                return 0
            depth = 1
            while node.left:
                depth += 1
                node = node.left
            return depth
        if not root:
            return 0
        left = getDepth(root.left)
        right = getDepth(root.right)
        if left == right:
            return 2**left + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2**right

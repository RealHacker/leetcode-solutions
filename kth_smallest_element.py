# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        self.buildTree(root)
        node = root
        while True:
            if k == node.t[0]+1:
                return node.val
            elif k<=node.t[0]:
                node = node.left
            else:
                k -= node.t[0]+1
                node = node.right
            
        
    def buildTree(self, root):
        if root.left is None:
            left = 0
        else:
            left = self.buildTree(root.left)
        if root.right is None:
            right = 0
        else:
            right = self.buildTree(root.right)
        root.t = (left, right)
        return left + right +1

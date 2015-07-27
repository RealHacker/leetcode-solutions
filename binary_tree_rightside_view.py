# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if not root:
            return []
        self.result = {}
        self.height = 0
        self.visit(root, 0)
        vals = []
        for i in range(self.height+1):
            vals.append(self.result[i])
        return vals
        
    def visit(self, node, lvl):
        if lvl > self.height:
            self.height = lvl
        if lvl not in self.result:
            self.result[lvl] = node.val
        if node.right:
            self.visit(node.right, lvl+1)
        if node.left:
            self.visit(node.left, lvl+1)
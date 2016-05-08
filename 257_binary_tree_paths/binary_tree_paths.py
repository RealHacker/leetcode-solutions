# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.paths = []
        self.visit(root, "")
        return self.paths
    
    def visit(self, node, current):
        if not node:
            return
        if current:
            current += "->"
        current += str(node.val)
        if not node.left and not node.right:
            self.paths.append(current)
        else:
            self.visit(node.left, current)
            self.visit(node.right, current)
        

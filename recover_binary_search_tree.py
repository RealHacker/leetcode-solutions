# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.lefty = None
        self.righty = None

        self._minnode = None
        self._maxnode = None

        self.preorder_visit(root)
        self.postorder_visit(root)
        print self.lefty, self.righty
        
        self.lefty.val, self.righty.val = self.righty.val, self.lefty.val


    def preorder_visit(self, node):
        # first check left and right trees
        if node.left:
            self.preorder_visit(node.left)
            if self.lefty:
                return

        if self._maxnode and node.val<self._maxnode.val:
            self.lefty = self._maxnode
            return
            
        if not self._maxnode or node.val > self._maxnode.val:
            self._maxnode = node

        if node.right:
            self.preorder_visit(node.right)
            
    def postorder_visit(self, node):
        # first check left and right trees
        if node.right:
            self.postorder_visit(node.right)
            if self.righty:
                return

        if self._minnode and node.val > self._minnode.val:
            self.righty = self._minnode
            return
        if not self._minnode or node.val < self._minnode.val:
            self._minnode = node

        if node.left:
            self.postorder_visit(node.left)

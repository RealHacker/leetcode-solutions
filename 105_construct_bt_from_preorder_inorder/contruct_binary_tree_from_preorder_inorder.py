# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        full_length = len(preorder)
        return self._buildTree(0, full_length, 0, full_length)
    
    def _buildTree(self, l1, h1, l2, h2):
        if l1 == h1:
            return
        node = TreeNode(self.preorder[l1])
        idx = self.inorder.index(self.preorder[l1])
        leftlen = idx-l2
        left = self._buildTree(l1+1, l1+1+leftlen, l2, l2+leftlen)
        right = self._buildTree(l1+1+leftlen, h1, l2+leftlen+1, h2)
        node.left = left
        node.right = right
        return node

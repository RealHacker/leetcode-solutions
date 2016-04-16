# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
            
        node = root
        left_root = None
        
        while node!=p:
            if node.val<p.val:
                node = node.right
            else:
                left_root = node
                node = node.left
        return left_root
        
                

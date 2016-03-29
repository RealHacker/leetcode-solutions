# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        newroot, oldroot = self.recurse(root)
        return newroot
    
    def recurse(self, root):
        if not root.left:
            return root, root
        newroot, oldroot = self.recurse(root.left)
        oldroot.left = root.right
        oldroot.right = root
        root.left = None
        root.right = None
        
        return newroot, root

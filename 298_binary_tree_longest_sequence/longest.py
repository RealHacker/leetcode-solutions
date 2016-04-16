# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self._max = 0
        self.recurse(root, 1, root.val)
        return self._max
    
    def recurse(self, node, depth, val):
        if not node:
            self._max = max(self._max, depth)
            return
        if node.val==val+1:
            self.recurse(node.left, depth+1, node.val)
            self.recurse(node.right, depth+1, node.val)
        else:
            self._max = max(self._max, depth)
            self.recurse(node.left, 1, node.val)
            self.recurse(node.right, 1, node.val)
            
            
        
        
                

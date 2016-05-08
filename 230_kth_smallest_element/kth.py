# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        _, val = self._recurse(root, k)
        return val
        
    def _recurse(self, node, k):
        # returns (Found or not, residue of k)
        # left tree
        if node.left:
            found, val = self._recurse(node.left, k)
            if found:
                return True, val
            else:
                k = val
                
        # deals with self
        if k==1:
            return True, node.val
        else:
            k = k-1
            
        # check the right tree
        if node.right:
            found, val = self._recurse(node.right, k)
            if found:
                return True, val
            else:
                k = val
        
        return False, k
            
            

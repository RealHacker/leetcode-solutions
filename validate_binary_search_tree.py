# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        a, b, c= self.recurse(root)
        return c
        
    def recurse(self, root):
        if not root.left and not root.right:
            return (root.val, root.val, True)
        min_ = root.val
        max_= root.val
        if root.left:
            if root.val<=root.left.val:
                return (None, None, False)
            else:
                _min, _max, ok = self.recurse(root.left)
                if not ok:
                    return (None, None, False)
                if _max>=root.val:
                    return (None, None, False)
                min_= min(min_, _min)
        if root.right:
            if root.val>=root.right.val:
                return (None, None, False)
            else:
                _min, _max, ok = self.recurse(root.right)
                if not ok:
                    return (None, None, False)
                if _min<=root.val:
                    return (None, None, False)
                max_= max(max_, _max)
        return (min_, max_, True)
        

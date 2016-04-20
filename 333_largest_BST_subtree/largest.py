# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.maxsize = 1
        self.recurse(root)
        return self.maxsize
        
    def recurse(self, node):
        # return 3 things:
        # 1. whether the subtree rooted at node is BST
        # 2. the smallest value in the subtree
        # 3. the largest value in the subtree
        if not node.left and not node.right:
            return (True, node.val, node.val, 1)
            
        is_BST = True
        _min = node.val
        _max = node.val
        size = 1
        if node.left:
            (is_left_BST, leftmin, leftmax, leftsize) = self.recurse(node.left)
            is_BST = is_BST and is_left_BST and node.val>leftmax
            _min = min(_min, leftmin)
            size += leftsize
        if node.right:
            (is_right_BST, rightmin, rightmax, rightsize) = self.recurse(node.right)
            is_BST = is_BST and is_right_BST and node.val<rightmin
            _max = max(_max, rightmax)
            size += rightsize
        if is_BST and size>self.maxsize:
            self.maxsize = size
        return is_BST, _min, _max, size
        

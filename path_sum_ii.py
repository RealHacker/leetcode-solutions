# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.results = []
        self.recurse(root, sum, [])
        return self.results
        
    def recurse(self, node, sum, partial):
        if not node:
            return
        if sum==node.val and node.left is None and node.right is None:
            self.results.append(partial+[node.val])
        else:
            if node.left:
                self.recurse(node.left, sum-node.val, partial+[node.val])
            if node.right:
                self.recurse(node.right, sum-node.val, partial+[node.val])

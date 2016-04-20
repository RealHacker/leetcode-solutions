# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
import operator

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.cols = defaultdict(list)
        self.recurse(root, 0, 0)
        print self.cols
        for k in self.cols:
            vs = self.cols[k]
            self.cols[k] = [v[1] for v in sorted(vs, key = operator.itemgetter(0))]
        pairs = sorted(self.cols.items(), key=operator.itemgetter(0))
        
        return [pair[1] for pair in pairs]
        
    def recurse(self, node, n, depth):
        # add the node itself into cols
        self.cols[n].append((depth,node.val))
        if node.left:
            self.recurse(node.left, n-1, depth+1)
        if node.right:
            self.recurse(node.right, n+1, depth+1)
        
        
        

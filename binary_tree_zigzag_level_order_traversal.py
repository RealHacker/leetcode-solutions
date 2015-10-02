# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.levels = []
        self.recurse(root, 0)
        result = []
        for i in range(len(self.levels)):
            level = self.levels[i]
            if i%2: level = level[::-1]
            result.append(level)
        return result
    
    def recurse(self, node, lvl):
        if not node:
            return
        if len(self.levels) <= lvl:
            self.levels.append([node.val])
        else:
            self.levels[lvl].append(node.val)
        self.recurse(node.left, lvl+1)
        self.recurse(node.right, lvl+1)


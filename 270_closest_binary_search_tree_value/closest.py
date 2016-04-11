# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        diff = sys.maxint
        closest = None
        node = root
        while True:
            if node is None:
                break
            if node.val==target:
                return node.val
            elif node.val>target:
                if diff>node.val-target:
                    diff = node.val-target
                    closest = node.val
                node = node.left
            else:
                if diff>target-node.val:
                    diff = target-node.val
                    closest = node.val
                node = node.right
        return closest

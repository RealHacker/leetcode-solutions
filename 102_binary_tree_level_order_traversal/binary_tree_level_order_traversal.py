# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root:
            return []
        self.q = deque()
        self.result = []
        self.q.append((root, 0))
        
        while self.q:
            node, lvl = self.q.popleft()
            if len(self.result)-1 < lvl:
                newlvl = [node.val]
                self.result.append(newlvl)
            else:
                self.result[lvl].append(node.val)
            if node.left:
                self.q.append((node.left, lvl+1))
            if node.right:
                self.q.append((node.right, lvl+1))
        return self.result
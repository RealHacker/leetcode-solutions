# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root==p or root==q:
            return root
        self.cnt = 0
        self.result = None
        self.dfs(root, p, q)
        return self.result
        
    def dfs(self, node, p, q):
        if not node:
            return 0
        ret1 = self.dfs(node.left, p, q)
        if ret1==2:
            return 2
        if node==p:
            ret1+=1
        if node==q:
            ret1+=1
        if ret1==2:
            self.result = node
            return 2
        else:
            ret2 = self.dfs(node.right, p, q)
            if ret2==2:
                return 2
        ret = ret1 + ret2
        
        if ret==2:
            self.result = node
        return ret
        
            
            

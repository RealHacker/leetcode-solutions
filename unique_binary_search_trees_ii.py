# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.buildTree(0, n)
        
    def buildTree(self, n1, n2):
        if n1==n2:
            return [None]
        if n1+1 == n2:
            node = TreeNode(n1+1)
            node.left = None
            node.right = None
            return [node]
        else:
            results = []
            for x in range(n1, n2):
                left_list = self.buildTree(n1, x)
                right_list = self.buildTree(x+1, n2)
                for left in left_list:
                    for right in right_list:
                        node = TreeNode(x+1)
                        node.left = left
                        node.right = right
                        results.append(node)
            return results

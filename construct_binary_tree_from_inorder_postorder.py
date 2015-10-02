# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder = inorder
        self.postorder = postorder
        return self.recurse(0, len(self.inorder), 0, len(self.postorder))
        
    def recurse(self, inleft, inright, postleft, postright):
        if inleft==inright:
            return None
        val = self.postorder[postright-1]
        idx = self.inorder.index(val)
        node = TreeNode(val)
        node.left = self.recurse(inleft, idx, postleft, postleft+idx-inleft)
        node.right = self.recurse(idx+1, inright, postleft+idx-inleft, postright-1)
        return node
        

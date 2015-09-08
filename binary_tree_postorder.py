# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            current = stack[-1]
            if not current.left and not current.right:
                result.append(stack.pop().val)
            else:
                if current.right:
                    stack.append(current.right)
                    current.right = None
                if current.left:
                    stack.append(current.left)
                    current.left = None
        return result
            
        

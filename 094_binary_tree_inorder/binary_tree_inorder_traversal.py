# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            item = stack.pop()
            if item is None:
                continue
            if isinstance(item, TreeNode):
                if not item.left and not item.right:
                    result.append(item.val)
                else:
                    stack.append(item.right)
                    stack.append(item.val)
                    stack.append(item.left)
            else:
                result.append(item)
        return result
        

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root: return None
        root.next = None
        self.recurse(root)
    
    def recurse(self, node):
        if not node or not node.left:
            return
        node.left.next = node.right
        if node.next:
            node.right.next = node.next.left
        else:
            node.right.next = None
        self.recurse(node.left)
        self.recurse(node.right)

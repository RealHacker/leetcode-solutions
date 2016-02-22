class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 and node2 or node1 and not node2:
            return False
        if node1.val != node2.val:
            return False
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
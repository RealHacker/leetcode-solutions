class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.p = p
        self.q = q
        ret, node = self.visit(root)
        return node
        
    def visit(self, node):
        if node == None:
            return 0, None
        ret1, node1 = self.visit(node.left)
        if ret1==2:
            return 2, node1
        ret2, node2 = self.visit(node.right)
        if ret2==2:
            return 2, node2
        foundself = (node==self.p or node==self.q)
        if ret1==1 and (ret2==1 or foundself):
            return 2, node
        if ret2==1 and foundself:
            return 2, node
        if ret1==1:
            return 1, node1
        if ret2==1:
            return 1, node2
        if foundself:
            return 1, node
        return 0, None

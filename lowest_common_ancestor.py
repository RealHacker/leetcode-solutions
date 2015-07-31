class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        self.pv = p.val
        self.qv = q.val
        self.visit(root)
        return self.result
        
    def visit(self, node):
        vals = [node.val]
        if node.left:
            vals.extend(self.visit(node.left))
        if node.right:
            vals.extend(self.visit(node.right))
        if self.pv in vals and self.qv in vals and not self.result:
            self.result = node
        return vals
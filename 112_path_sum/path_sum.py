class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        elif not root.left:
            return self.hasPathSum(root.right, sum-root.val)
        elif not root.right:
            return self.hasPathSum(root.left, sum-root.val)
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

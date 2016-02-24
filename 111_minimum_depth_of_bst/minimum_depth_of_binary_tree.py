class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minDepth(root.right)+1
        elif not root.right:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1

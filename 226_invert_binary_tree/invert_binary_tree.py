class Solution:

    # @param {TreeNode} root

    # @return {TreeNode}

    def invertTree(self, root):
	if not root:
		return
	root.left, root.right = root.right, root.left
	self.invertTree(self.left)
	self.invertTree(self.right)
	

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        self.compute_height(root)
        def get_balance(node):
            if not node:
                return True
            if node.left:
                l = node.left.height
            else:
                l = 0
            if node.right:
                r = node.right.height
            else:
                r = 0
            if abs(l-r)>1:
                return False
            return get_balance(node.left) and get_balance(node.right) 
        return get_balance(root)
    
    def compute_height(self, node):
        if not node:
            return 0
        
        left = self.compute_height(node.left)
        right = self.compute_height(node.right)
        height = max(left, right)+1
        node.height = height
        return height

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.recurse(root)
        
    def recurse(self, root):
        # return the head and tail of flattened list
        if not root.left and not root.right:
            return root, root
        if not root.left and root.right:
            r, last = self.recurse(root.right)
            return root, last
        elif not root.right and root.left:
            l, last = self.recurse(root.left)
            root.right = l
            root.left = None
            return root, last
        else:
            l, llast = self.recurse(root.left)
            r, rlast= self.recurse(root.right)
            root.right = l
            llast.right = r
            rlast.right = None
            return root, rlast
            

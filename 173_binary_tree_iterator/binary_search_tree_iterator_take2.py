# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if not root: 
            self.stack = []
            return
        self.stack = [root]
        while self.stack[-1].left:
            self.stack.append(self.stack[-1].left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)!=0

    def next(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        val = self.stack[-1].val
        if self.stack[-1].right:
            self.stack.append(self.stack[-1].right)
            while self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        else:
            node = self.stack.pop()
            while self.stack and node==self.stack[-1].right:
                node = self.stack.pop()
        return val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

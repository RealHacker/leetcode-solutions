# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        if not root:
            self.head = self.tail = None
        else:
            self.head, self.tail = self.flatten(root)
    
    def flatten(self, node):
        if not node.left:
            head = node
        else:
            h, t = self.flatten(node.left)
            t.right = node
            head = h
        if not node.right:
            tail = node
        else:
            h, t = self.flatten(node.right)
            node.right = h
            tail = t
        return head, tail
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.head 

    # @return an integer, the next smallest number
    def next(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.right
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        self.in_order = []
        self.inorder_traverse(root)
        for i, node in enumerate(self.in_order[:-1]):
            node.right = self.in_order[i+1]
        if self.in_order:
            self.in_order[-1].right = None
        
    def inorder_traverse(self, root):
        if not root:
            return
        else:
            self.in_order.append(root)
            self.inorder_traverse(root.left)
            self.inorder_traverse(root.right)

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def make_tree(_list):
    if not _list:
        return
    val = _list.pop(0)
    if not val:
        return None
    node = TreeNode(val)
    node.left = make_tree(_list)
    node.right = make_tree(_list)
    return node

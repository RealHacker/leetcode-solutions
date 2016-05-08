# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # First get to the bottom of tree for its depth
        depth = 0
        node = root
        while node:
            depth += 1
            node = node.left
        
        if depth<=1:
            return depth
        # count the number of leaves with bfs
        self.leaves = 0
        self.visit(root, depth)
            
        # add the internal nodes
        return 2**(depth-1)-1+self.leaves
            
    def visit(self, node, depth):
        if node.left and node.right:
            more = self.visit(node.left, depth-1)
            if more:
                return self.visit(node.right, depth-1)
            else:
                return False
        elif node.left:
            self.leaves+=1
            return False
        else:
            # this is a leaf
            if depth==1:
                self.leaves+=1
                return True
            else:
                return False
                
            
        

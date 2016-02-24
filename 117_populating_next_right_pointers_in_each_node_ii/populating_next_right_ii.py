# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        root.next = None
        self.recurse(root)
    
    def recurse(self, root):
        level = []
        if root.left:
            level.append(root.left)
        if root.right:
            level.append(root.right)
        cur = root
        while cur.next:
            if cur.next.left:
                level.append(cur.next.left)
            if cur.next.right:
                level.append(cur.next.right)
            cur = cur.next
        if not level:
            return
        for i in range(len(level)):
            if i==len(level)-1:
                level[i].next = None
            else:
                level[i].next = level[i+1]
        self.recurse(level[0])
            
            
            

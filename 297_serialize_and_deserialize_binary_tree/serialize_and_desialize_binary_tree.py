# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        return "["+str(root.val)+","+self.serialize(root.left)+","+self.serialize(root.right)+"]"
        
    def getSection(self, data):
        brackets = 1
        idx = 1
        while brackets != 0:
            if data[idx]=="[":
                brackets+=1
            elif data[idx]=="]":
                brackets-=1
            idx+=1
        return data[:idx],idx
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data=="null":
            return None
        first_comma = data.index(",")
        val = int(data[1:first_comma])
        data = data[first_comma+1:]
        if data[0]=="[":
            leftsection, last = self.getSection(data)
            left = self.deserialize(leftsection)
        else:
            last = 4
            left = None
            
        data = data[last+1:]
        if data[0]=="[":
            rightsection,_ = self.getSection(data)
            right = self.deserialize(rightsection)
        else:
            right = None
            
            
        node = TreeNode(val)
        node.left = left
        node.right = right
        
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

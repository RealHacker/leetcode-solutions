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
            return json.dumps(None)
        obj = {
            "root": root.val,
            "left": self.serialize(root.left),
            "right": self.serialize(root.right)
        }
        return json.dumps(obj)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d = json.loads(data)
        if not d: return None
        node = TreeNode(d["root"])
        node.left = self.deserialize(d["left"])
        node.right = self.deserialize(d["right"])
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

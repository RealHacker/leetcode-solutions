# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        tree = self.recurse(nums)
        return tree
        
    def recurse(self, nums):
        if not nums:
            return None
        if len(nums)==1:
            node = TreeNode(nums[0])
            node.left = node.right = None
        mid = len(nums)/2
        left = self.recurse(nums[:mid])
        right = self.recurse(nums[mid+1:])
        node = TreeNode(nums[mid])
        node.left = left
        node.right = right
        return node

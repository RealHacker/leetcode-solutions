# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, x):

#         self.val = x

#         self.next = None



class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
	def deleteNode(self, node):
		current = node
		node = node.next
		while node.next:
			current.val = node.val
			current = node
			node = node.next
		current.val = node.val
		current.next = None
		
			
			
				

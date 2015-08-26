# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        current = head
        p = head.next
        
        while p:
            if p.val != current.val:
                current.next = p
                current = p
            p = p.next
        current.next = p
        return head
                
    
    
    
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        newHead = None
        tail = None
        p1 = head
        p2 = head.next
        while p1 and p2:
            p1.next = p2.next
            p2.next = p1
            if newHead:
                tail.next = p2
            else:
                newHead = p2
            tail = p1
            
            p1 = p1.next
            if p1:
                p2 = p1.next
                
        return newHead

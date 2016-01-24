# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        odd = oddtail = head
        even =eventail = head.next
        cur = even.next
        i=0
        while cur:
            if i%2==0:
                oddtail.next = cur
                oddtail = cur
            else:
                eventail.next = cur
                eventail = cur
            i+=1
            cur = cur.next
        oddtail.next = even
        eventail.next = None
        return odd
        
            

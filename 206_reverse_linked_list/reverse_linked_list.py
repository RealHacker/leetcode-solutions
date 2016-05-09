class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        a = head
        b = a.next
        c = b.next
        a.next = None
        while True:
            b.next = a
            a = b
            b = c

            if c:
                c = c.next
            if b is None:
                break
        return a

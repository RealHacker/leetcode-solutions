# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        prev = None
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = slow.next
            slow.next = None
        else:
            head = head.next
        return head

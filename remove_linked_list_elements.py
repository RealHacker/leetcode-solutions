# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        if head:
            p1 = head
            p2 = head.next
            while p2:
                if p2.val == val:
                    p1.next = p2.next
                    p2 = p2.next
                else:
                    p1 = p2
                    p2 = p2.next
        return head

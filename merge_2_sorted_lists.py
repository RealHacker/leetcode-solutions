# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val>l2.val:
            l1, l2 = l2, l1
        cur = l1
        precur = None
        while l2:
            while cur and l2.val>=cur.val:
                precur = cur
                cur = cur.next
            node = l2
            l2 = l2.next
            precur.next = node
            node.next = cur
            precur = node
        return l1

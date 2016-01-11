# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        idx = 1
        h = None
        p = head
        vals = []
        while True:
            if idx==m:
                h = p
            if idx>=m and idx<=n:
                vals.append(p.val)
            if idx==n:
                break
            idx = idx +1
            p = p.next
        while h!=p.next:
            h.val = vals.pop()
            h = h.next
        return head

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
        
        newhead = newtail = None
        seen = dict()
        p = head
        pp = None
        while p:
            dup = False
            while p.next and p.next.val==p.val:
                dup = True
                p = p.next
            if not dup:
                if not newhead:
                    newhead=newtail= p
                else:
                    newtail.next = p
                    newtail = p
            p = p.next
        if newtail:
            newtail.next = None
        return newhead
                

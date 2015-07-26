# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        ptr = head
        tail = None
        while ptr != None:
            cnt = 0
            segment = ptr
            while cnt < k and ptr != None:
                ptr = ptr.next
                cnt += 1
            if cnt < k:
                if tail:
                    tail.next = segment
            else:
                h, t = self.reverseGroup(segment, ptr)
                if t == head:
                    head = h
                else:
                    tail.next = h
                tail = t
        return head
    
    def reverseGroup(self, head, ptr):
        newtail = head
        p1 = head
        p2 = head.next
        
        newtail.next = None  # just to be safe
        while p2 != ptr:
            temp = p2
            p2 = p2.next
            temp.next = p1
            p1 = temp
        return p1, newtail

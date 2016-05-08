# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
            
        if not head.next:
            return True
            
        _len = 0
        fast = slow = head
        while fast:
            slow = slow.next
            _len+=1
            if fast.next:
                fast = fast.next.next
            else:
                break
        half = slow
        while slow:
            slow = slow.next
            _len+=1
        
        right = half

        p = right
        pp = None
        while p:
            temp = p.next
            p.next = pp
            pp = p
            p = temp
        
        p = head
        while pp:
            if p.val!=pp.val:
                return False
            p = p.next
            pp = pp.next
        
        return True
        

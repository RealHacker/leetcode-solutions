# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        cursor= head
        precursor = None
        head1 = tail1 = None
        head2 = tail2 = None
        
        while cursor:
            if cursor.val < x:
                if not head1:
                    head1 = cursor
                    tail1 = cursor
                else:
                    tail1.next = cursor
                    tail1 = tail1.next
                if tail2:
                    tail2.next = cursor.next
            else:
                if not head2:
                    head2 = cursor
                tail2 = cursor
            cursor = cursor.next
        if tail1:
            tail1.next = None
        if tail2:
            tail2.next = None
        if not head1:
            return head2
        else:
            tail1.next = head2
            return head1
            
                
                
                
                
                
                
                
                

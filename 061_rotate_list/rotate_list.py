class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        n = 0
        cursor = head
        while cursor:
            cursor = cursor.next
            n += 1
        k = k%n
        if k==0: return head
            
        fast = slow = head
        for i in range(k):
            if fast:
                fast = fast.next
            else: 
                break
        preslow = None
        prefast = None
        while fast:
            prefast = fast
            fast = fast.next
            preslow = slow
            slow = slow.next
        if preslow:
            prefast.next = head
            preslow.next = None
            return slow
        else:
            return head

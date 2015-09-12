
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                break
        else:
            return None
        fast = slow.next
        p = head
        n1 = 0
        while p!=slow:
            p = p.next
            n1+=1
        n2 = 0
        while fast!=slow:
            fast = fast.next
            n2+=1
        
        fast = slow.next
        if n1>n2:
            while n1!=n2:
                head = head.next
                n1-=1
        elif n1<n2:
            while n1!=n2:
                fast = fast.next
                n2-=1
                
        while fast != head:
            fast = fast.next
            head = head.next
        return head
                

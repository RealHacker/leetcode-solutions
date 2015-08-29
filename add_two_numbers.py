class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        tail = head = None
        while True:
            if not l1 and not l2:
                break
            
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            if not l2:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            
            if carry+val1+val2>=10:
                val = (carry+val1+val2)%10
                carry = 1
            else:
                val = (carry+val1+val2)
                carry = 0
                
                
            node = ListNode(val)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = node
                
        if carry:
            node = ListNode(1)
            tail.next = node
            tail = node
        tail.next = None
        
        return head

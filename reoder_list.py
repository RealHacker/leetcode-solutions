class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        stack = []
        p = head
        cnt = 0
        while p:
            stack.append(p)
            p = p.next
            cnt +=1
        cnt = cnt/2
        p = head
        q = stack.pop()

        while cnt>0:
            q.next = p.next
            p.next = q
            p = p.next.next
            q = stack.pop()
            cnt -=1
        p.next = None

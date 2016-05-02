class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        return self.recurse(head)
    
    def recurse(self, node):
        if not node.next:
            return node
        # split into 2
        slow = node
        fast = node
        while fast and fast.next:
            preslow = slow
            slow = slow.next
            fast = fast.next.next
        preslow.next = None
        
        list1 = self.recurse(node)
        list2 = self.recurse(slow)
        
        if list2.val<list1.val:
            list1, list2 = list2, list1
        cur = list1
        pre = None
        while list2:
            while cur and cur.val<=list2.val:
                pre = cur
                cur = cur.next
            node = list2
            list2 = list2.next
            node.next = cur
            pre.next = node
            pre = node
            
            
        return list1


class Node:
    pass

node1 = Node()
node1.val = 3
node2 = Node()
node2.val = 2
node3 = Node()
node3.val = 4
node1.next = node2
node2.next = node3
node3.next = None


n = Solution().sortList(node1)
print n.val, n.next.val, n.next.next.val

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printNode(self):
        cur = self
        print cur.val
        print "->"
        if self.next:
            self.next.printNode()

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        # first put all nodes in a list
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        head = None
        tail = None
        for node in nodes:
            if not head:
                head = node
                tail = node
                head.next = None
                continue
            if tail.val<node.val:
                tail.next = node
                node.next = None
                tail = node
                continue
            cur1 = None
            cur2 = head
            while cur2 and cur2.val < node.val:
                cur1 = cur2
                cur2 = cur2.next
            node.next = cur2
            if not cur2:
                tail = node
            if not cur1:
                head = node
            else:
                cur1.next = node
        return head


node0 = ListNode(1)
node1 = ListNode(1)

node0.next = node1

n = Solution().insertionSortList(node0)
n.printNode()
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        if not head.next:
            node = TreeNode(head.val)
            node.left = None
            node.right = None
            return node
        fast = slow = head
        preslow = None
        while fast and fast.next:
            fast = fast.next.next
            preslow = slow
            slow = slow.next
        preslow.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        def len(node):
            i = 0
            while node:
                i+=1
                node = node.next
            return i
        diff = len(headA) - len(headB)
        while diff > 0:
            headA = headA.next
            diff -= 1
        while diff < 0:
            headB = headB.next
            diff += 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
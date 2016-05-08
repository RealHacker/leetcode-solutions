# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        s = []
        while head != None:
            s.append(head.val)
            head = head.next
        return s == list(reversed(s))

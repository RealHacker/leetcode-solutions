class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        return self.mergeN(lists)
        
    def mergeN(self, lists):
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.merge(lists[0], lists[1])
        front = self.mergeN(lists[:len(lists)/2])
        back = self.mergeN(lists[len(lists)/2:])
        return self.merge(front, back)
         
    def merge(self, res, lst):
        if not res:
            return lst
        if not lst:
            return res
        if lst.val<res.val:
            nxt = lst.next
            lst.next = res
            res = lst
            lst = nxt
        prev = ptr = res
        while lst:
            while ptr and ptr.val<=lst.val:
                prev = ptr
                ptr = ptr.next
            nxt = lst.next
            lst.next = ptr
            prev.next = lst
            lst = nxt
            prev = prev.next
                
        return res

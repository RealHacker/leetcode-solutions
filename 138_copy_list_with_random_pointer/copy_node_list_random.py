# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        p = head
        np = RandomListNode(head.label)
        p.link = np
        if p.random:
            if p.random==p:
                np.random = np
            else:
                p.random.pending = [np]
                
        p1 = p
        p2 = p1.next
        np1 = np
        while p2:
            np2 = RandomListNode(p2.label)
            p2.link = np2
            
            np1.next = np2
            if hasattr(p2, "pending"):
                for x in p2.pending:
                    x.random = np2
            
            # check random
            randomNode = p2.random
            if randomNode:
                if hasattr(randomNode, "link"):
                    np2.random = randomNode.link
                else:
                    if not hasattr(randomNode, "pending"):
                        randomNode.pending = []
                    randomNode.pending.append(np2)
                
            p1 = p2
            p2 = p2.next
            np1 = np2
        
        return np
            
        
            
            

class Solution(object):
    class PairingHeap(object):
        def __init__(self, freqency, children, parent, val):
            self.fre = freqency
            self.children = children
            self.parent = parent
            self.val = val
        def increment_fre(self):
            self.fre += 1
        def __repr__(self):
            return "%s %s, %s %s"%(self.fre, [c.val for c in self.children], self.parent.val, self.val)
            
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # implementation with pairing heap
        heap = None
        # a heap is a 3-tuple: (val, children set, parent)
        registry = {}
        for num in nums:
            # increment the heap's value
            if num not in registry:
                newheap = self.PairingHeap(1, set(), None, num)
                registry[num] = newheap
            else:
                newheap = registry[num]
                newheap.increment_fre()
            # merge the heap into main
            if not heap:
                heap = newheap
            else:
                if newheap.parent:
                    if newheap.fre<=newheap.parent.fre:
                        continue
                    newheap.parent.children.remove(newheap)
                    newheap.parent = None
                # insert only when newheap is not root
                if newheap!=heap:
                    if newheap.fre<=heap.fre:
                        newheap.parent = heap
                        heap.children.add(newheap)
                    else:
                        heap.parent = newheap
                        newheap.children.add(heap)
                        heap = newheap
        # print heap
        # get the maximums from the heap
        results = []
        while heap and len(results)<k:
            #if not results or heap.fre!=results[-1].fre:
            results.append(heap)
            heap = self.mergeheap(heap.children)
        results = [result.val for result in results]
        return results
            
    def mergeheap(self, heaps):
        heaps = list(heaps)
        if not heaps:
            return None
        if len(heaps) ==1:
            return heaps[0]  
        elif len(heaps)==2:
            if heaps[0].fre<=heaps[1].fre:
                heaps[1].children.add(heaps[0])
                heaps[0].parent = heaps[1]
                return heaps[1]
            else:
                heaps[0].children.add(heaps[1])
                heaps[1].parent = heaps[0]
                return heaps[0]
        else:
            half = len(heaps)/2
            return self.mergeheap([self.mergeheap(heaps[:half]), self.mergeheap(heaps[half:])])
            

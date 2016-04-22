import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.minheap or num>self.minheap[0]:
            heapq.heappush(self.minheap, num)
        elif not self.maxheap or num<-self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            if len(self.minheap)>len(self.maxheap)+1:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        
        # now make it balanced
        while len(self.minheap)>len(self.maxheap)+1:
            item = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -item)
            
        while len(self.maxheap)>len(self.minheap):
            item = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -item)
            
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.maxheap and not self.minheap:
            return None
        if len(self.maxheap)==len(self.minheap):
            return (self.minheap[0]-self.maxheap[0])*1.0/2
        else:
            return self.minheap[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

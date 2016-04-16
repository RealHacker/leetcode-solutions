class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.index = 0
        self.numbers = [v1, v2]
        self.positions = [0,0]

    def next(self):
        """
        :rtype: int
        """
        v = self.numbers[self.index]
        pos = self.positions[self.index]
        if pos<len(v):
            value = v[pos]
            self.positions[self.index]+=1
            self.index = (self.index+1)%2
            return value
        else:
            if self.hasNext():
                self.index = (self.index+1)%2
                return self.next()
            else:
                return None
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return any([self.positions[i]<len(self.numbers[i]) for i in range(2)])

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

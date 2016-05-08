from collections import deque
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.standing = None
        self.q = deque()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.standing:
            self.q.append(self.standing)
        self.standing = x
        
    # @return nothing
    def pop(self):
        self.standing = None
        if self.q and len(self.q)>0:
            newq = deque()
            for i in range(len(self.q)-1):
                newq.append(self.q.popleft())
            self.standing = self.q.popleft()
            self.q = newq

    # @return an integer
    def top(self):
        return self.standing
        
    # @return an boolean
    def empty(self):
        return self.standing is None and len(self.q) == 0

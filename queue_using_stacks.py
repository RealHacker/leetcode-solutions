class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q1.append(x)
        
    # @return nothing
    def pop(self):
        if self.q2:
            self.q2.pop()
        else:
            while True:
                try:
                    item = self.q1.pop()
                except:
                    break
                else:
                    self.q2.append(item)
            self.q2.pop()
        
    # @return an integer
    def peek(self):
        if self.q2:
            return self.q2[-1]
        else:
            while True:
                try:
                    item = self.q1.pop()
                except:
                    break
                else:
                    self.q2.append(item)
            return self.q2[-1]

    # @return an boolean
    def empty(self):
        return (not self.q1) and (not self.q2)
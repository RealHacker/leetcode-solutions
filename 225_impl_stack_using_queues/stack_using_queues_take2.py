class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.q1)>1:
            item = self.q1.pop(0)
            self.q2.append(item)
        val = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1)>1:
            item = self.q1.pop(0)
            self.q2.append(item)
        val = self.q1.pop(0)
        self.q2.append(val)
        self.q1, self.q2 = self.q2, self.q1
        return val

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q1)==0
        

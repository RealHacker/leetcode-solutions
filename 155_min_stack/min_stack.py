class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.nums = []
        self.mins = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.nums.append(x)
        if self.mins:
            if x<self.nums[self.mins[-1]]:
                self.mins.append(len(self.nums)-1)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(0)
        
        
    # @return nothing
    def pop(self):
        if self.nums:
            del self.nums[-1]
            del self.mins[-1]
        

    # @return an integer
    def top(self):
        return self.nums[-1]

    # @return an integer
    def getMin(self):
        return self.nums[self.mins[-1]]

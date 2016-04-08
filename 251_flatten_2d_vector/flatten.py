class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.end_reached = False
        if not vec2d:
            self.end_reached = True
        else:
            self.x = self.y = 0
            self.advance()
    
    def advance(self):
        if self.end_reached: return
        while True:
            if self.y < len(self.vec[self.x]):
                break
            self.x += 1
            self.y = 0
            if self.x >= len(self.vec):
                self.end_reached = True
                break
        

    def next(self):
        """
        :rtype: int
        """
        self.advance()
        if self.end_reached: return None
        
        val = self.vec[self.x][self.y]
        self.y += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        self.advance()
        return not self.end_reached

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

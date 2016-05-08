import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.list = []
        self.squares = {}
        i = 1
        while i*i<=n:
            self.list.append(i*i)
            self.squares[i*i]=1
            i+=1
        if n in self.squares:
            return 1
        return self.recurse(n)
        
    def recurse(self, n):
        q = [(n, 0)]
        visited = set()
        while q:
            item, extra = q.pop(0)
            if item in self.squares:
                m = self.squares[item]+extra
                return m
            else:
                for i in self.list:
                    if i>=item:
                        break
                    if item-i not in visited:
                        q.append((item-i, extra+1))
                        visited.add(item-i)
                

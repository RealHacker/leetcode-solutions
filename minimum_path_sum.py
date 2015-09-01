import sys
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.memo = {}
        return self.minPath(grid, 0,0)
        
    def minPath(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        
        if (x, y) in self.memo:
            return self.memo[(x,y)]
        
        if x ==n-1 and y==m-1:
            return grid[n-1][m-1]
            
        if x < n-1:
            right = self.minPath(grid, x+1, y)
        else:
            right = sys.maxint
            
        if y < m-1:
            down = self.minPath(grid, x, y+1)
        else:
            down = sys.maxint
            
        self.memo[(x, y)] = min(down, right)+grid[x][y]
        
        return self.memo[(x, y)]

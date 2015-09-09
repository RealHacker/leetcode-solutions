class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                   count +=1
                   self.sink(grid, i, j)
        return count
                
    def sink(self, grid, i, j):
        if j>0 and grid[i][j-1]=='1':
            grid[i][j-1]=0
            self.sink(grid, i, j-1)
        if j+1<len(grid[0]) and grid[i][j+1]=='1':
            grid[i][j+1]=0
            self.sink(grid, i, j+1)
        if i>0 and grid[i-1][j]=='1':
            grid[i-1][j]=0
            self.sink(grid, i-1, j)
        if i+1<len(grid) and grid[i+1][j]=='1':
            grid[i+1][j]=0
            self.sink(grid, i+1, j)


g1 = [
[c for c in "11000"],
[c for c in "11000"],
[c for c in "00100"],
[c for c in "00011"],
]

g2 = [
[c for c in "11110"],
[c for c in "11010"],
[c for c in "11001"],
[c for c in "00011"],
]
print Solution().numIslands(g1)
print Solution().numIslands(g2)

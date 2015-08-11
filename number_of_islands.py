class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0
        leaders = {}
        d ={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    if i>0 and grid[i-1][j]=='1' and (i-1, j) in d:
                        d[(i, j)] = d[(i-1,j)]
                        leaders[d[(i,j)]].append((i, j))
                    if j>0 and grid[i][j-1]=='1' and (i, j-1) in d:
                        if (i, j) in d and d[(i,j)]!=d[(i,j-1)]:
                            # merge
                            leader1 = d[(i, j)]
                            leader2 = d[(i,j-1)]
                            for c in leaders[leader2]:
                                d[c] = leader1
                                leaders[leader1].append(c)
                            del leaders[leader2]
                        else:
                            d[(i,j)] = d[(i, j-1)]
                            leaders[d[(i,j)]].append((i, j))
                    if (i,j) not in d:
                        leaders[(i,j)]=[]
                        d[(i, j)]=(i,j)
        return len(leaders)

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

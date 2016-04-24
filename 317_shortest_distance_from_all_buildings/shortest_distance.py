class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        # find the houses
        houses = []
        idx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    houses.append((i, j, idx))
                    idx +=1
        # BFS
        q = [(i, j, idx, 0) for i, j, idx in houses]
        distances = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                vec = []
                if grid[i][j]==0:
                    vec = [-1] * len(houses)
                row.append(vec)
            distances.append(row)
            
        while q:
            i, j, idx, dis = q.pop(0)
            for dx, dy in [(0,1),(1,0),(-1,0), (0,-1)]:
                x, y = i+dx, j+dy
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==0 and distances[x][y][idx]<0:
                    distances[x][y][idx] = dis+1
                    q.append((x, y, idx, dis+1))
            
        # calculate distance
        min_dist = sys.maxint
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                vec = distances[i][j]
                d = sum(vec) if vec and all([v>0 for v in vec]) else sys.maxint
                min_dist = min(min_dist, d)
        
        if min_dist == sys.maxint:
            min_dist = -1
        return min_dist

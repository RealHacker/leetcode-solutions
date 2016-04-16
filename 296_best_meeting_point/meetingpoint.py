class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rows.append(i)
                    cols.append(j)
        rows.sort()
        cols.sort()
        distance_x = sum([abs(x-rows[len(rows)/2]) for x in rows])
        distance_y = sum([abs(y-cols[len(cols)/2]) for y in cols])
        return distance_x + distance_y
                

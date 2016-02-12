class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # classical DP
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        mat = [[0 for i in range(m)] for j in range(n)]
        
        # first row
        blocked = False
        for i in range(m):
            if obstacleGrid[0][i]==1:
                blocked = True
            mat[0][i]=1 if not blocked else 0
        
        # first column
        blocked = False
        for i in range(n):
            if obstacleGrid[i][0]==1:
                blocked = True
            mat[i][0]=1 if not blocked else 0
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    mat[i][j] = 0
                else:
                    mat[i][j] = mat[i-1][j]+mat[i][j-1]
        
        return mat[-1][-1]

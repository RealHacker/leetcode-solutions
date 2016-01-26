class Solution(object):

    def longestIncreasingPath(self, matrix):

        """

        :type matrix: List[List[int]]

        :rtype: int

        """

        self.dp = {}

        def dp(x, y):

            if (x, y) not in self.dp:

                self.dp[(x, y)] = 1+max(

                    dp(x+1, y) if x+1<len(matrix) and matrix[x+1][y]<matrix[x][y] else 0,

                    dp(x-1, y) if x>0 and matrix[x-1][y]<matrix[x][y] else 0,

                    dp(x, y+1) if y+1<len(matrix[0]) and matrix[x][y+1]<matrix[x][y] else 0,

                    dp(x, y-1) if y>0 and matrix[x][y-1]<matrix[x][y] else 0

                )

            return self.dp[(x, y)]

        m = 0

        for i, row in enumerate(matrix):

            for j, c in enumerate(row):

                m = max(m, dp(i, j))

        return m

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:return
        firstRowContainsZero = 0 in matrix[0]
        firstColContainsZero = 0 in [matrix[x][0] for x in range(len(matrix))]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if firstRowContainsZero:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0
        if firstColContainsZero:
            for x in range(len(matrix)):
                matrix[x][0] = 0

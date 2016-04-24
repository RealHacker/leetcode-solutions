class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if matrix:
            row0 = []
            sum = 0
            for val in matrix[0]:
                sum += val
                row0.append(sum)
            self.sums = [row0]
            sum = row0[0]
            for i in range(1, len(matrix)):
                sum += matrix[i][0]
                row = [sum] + [0]*(len(matrix[0])-1)
                self.sums.append(row)
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    self.sums[i][j] = matrix[i][j] + self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1]
            #print self.sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix: return 0
        sum = self.sums[row2][col2]
        if row1>0:
            sum -= self.sums[row1-1][col2]
        if col1>0:
            sum -= self.sums[row2][col1-1]
        if row1>0 and col1>0:
            sum += self.sums[row1-1][col1-1]
        return sum
        
# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)

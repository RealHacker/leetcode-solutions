import bisect
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row = bisect.bisect_left([r[0] for r in matrix], target)
        if row == len(matrix):
            row = row-1
        else:
            if matrix[row][0]==target:
                return True
            else:
                row = row-1
        col = bisect.bisect_left(matrix[row], target)
        if col == len(matrix[0]):
            return False
        else:
            return matrix[row][col] == target
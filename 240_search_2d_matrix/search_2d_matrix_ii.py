import bisect
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        idx = rowlen = len(matrix[0])
        for row in matrix:
            row = row[:idx]
            newidx = bisect.bisect_left(row, target)
            if newidx<idx and row[newidx]==target:
                return True
            idx = newidx
        return False

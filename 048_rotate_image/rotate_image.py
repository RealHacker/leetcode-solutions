class Solution:

    # @param {integer[][]} matrix

    # @return {void} Do not return anything, modify matrix in-place instead.

    def rotate(self, matrix):

        matrix.reverse()

        for i in range(len(matrix)-1):

                for j in range(i+1, len(matrix)):

                        a, b = matrix[j][i] , matrix[i][j]

                        matrix[j][i] = b

                        matrix[i][j] = a

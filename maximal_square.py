class Solution:
    # @param {character[][]} matrix
    # @return {integer}
        def maximalSquare(self, matrix):
                if not matrix:
                        return 0
                max_square = 0
                self.visited = []
                for line in matrix:
                        row = []
                        for c in line:
                                row.append(0)
                        self.visited.append(row)
                self.visited[0] = [int(c) for c in matrix[0]]
                max_square = max(self.visited[0])
                for i, row in enumerate(self.visited):
                        k = int(matrix[i][0])
                        if k > max_square: 
                            max_square = k
                        row[0] = k
                for i in range(1, len(matrix)):
                        for j in range(1, len(matrix[0])):
                                if matrix[i][j]=='1':
                                    self.visited[i][j] = min(self.visited[i-1][j], self.visited[i][j-1], self.visited[i-1][j-1])+1
                                    if self.visited[i][j]> max_square:
                                        max_square = self.visited[i][j]
                return max_square**2
			
				

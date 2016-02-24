class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
    	self.memo = {}
    	def get_min(row, col):
    		if (row, col) in self.memo:
    			return self.memo[(row, col)]
    		if row == len(triangle) -1:
    			return triangle[row][col]
    		else:
    			minval = triangle[row][col]+ min(get_min(row+1, col), get_min(row+1, col+1))
    			self.memo[(row, col)] = minval
    			return minval
    	return get_min(0,0)


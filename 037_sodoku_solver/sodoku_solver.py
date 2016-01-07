class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.blanks = []
        for i in range(9):
        	for j in range(9):
        		if board[i][j]==".":
        			self.blanks.append((i,j))
        self.solve(0)


    def solve(self, k):
    	if k == len(self.blanks):
    		return True
    	i, j = self.blanks[k]
    	choices = set(['1', '2', '3', '4','5', '6', '7', '8', '9'])
    	row = set(self.board[i])
    	col = set([self.board[n][j] for n in range(9)])
    	x, y = i/3, j/3
    	square = []
    	for ii in range(x*3, x*3+3):
    		for jj in range(y*3, y*3+3):
    			square.append(self.board[ii][jj])
    	square = set(square)
    	choices = choices-row-col-square
    	print choices
    	if not choices:
    		return False
    	for choice in choices:
    		self.board[i][j] = choice
    		if self.solve(k+1):
    			return True




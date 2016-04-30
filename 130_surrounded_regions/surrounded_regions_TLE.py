class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return 
        lx = len(board)
        ly = len(board[0])
        for x in range(lx):
            for y in range(ly):
                if board[x][y] == 'O':
                    self.area = []
                    if self.explore(board, x, y):
                        for xx, yy in self.area:
                            board[xx][yy]='X'
                        
    
    def explore(self, board, x, y):
        if board[x][y]!="O":
            return True
        if x == 0 or x==len(board)-1 or y==0 or y==len(board[0])-1:
            return False
        if (x, y) in self.area:
            return True
        self.area.append((x, y))
        return self.explore(board, x, y+1) and self.explore(board, x+1, y) and self.explore(board, x-1, y) and self.explore(board, x, y-1)
        
        

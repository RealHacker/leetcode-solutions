class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board:
            return 
        lx = len(board)
        ly = len(board[0])
        # first last column and row
        for x in range(lx):
            self.explore(board, x, 0)
            self.explore(board, x, ly-1)
        for y in range(ly):
            self.explore(board, 0, y)
            self.explore(board, lx-1, y)
        
        for x in range(lx):
            for y in range(ly):
                if board[x][y] == 'I':
                    board[x][y]='O'
                else:
                    board[x][y]='X'
                        
    def explore(self, board, x, y):
        q = [(x, y)]
        while q:
            x, y = q.pop(0)
            if x < 0 or x>len(board)-1 or y<0 or y>len(board[0])-1:
                continue 
            if board[x][y]!="O":
                continue
            board[x][y]='I'
            q.append((x, y+1))
            q.append((x+1, y))
            q.append((x-1, y))
            q.append((x, y-1))

        
        

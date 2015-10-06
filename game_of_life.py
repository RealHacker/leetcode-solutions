class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        def getNeighbours(b, x, y):
            width = len(b[0])
            height = len(b)
            candidates = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
            count = 0
            for xx, yy in candidates:
                if xx<0 or xx>=height:continue
                if yy<0 or yy>=width: continue
                if b[xx][yy]:
                    count+=1
            return count
        
        nextboard = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = getNeighbours(board, i, j)
                if board[i][j]:
                    if n==2 or n==3:
                        nextboard[i][j] = 1
                else:
                    if n==3:
                        nextboard[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=nextboard[i][j]
                

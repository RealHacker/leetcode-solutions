class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dirs = [(1,0),(0,1),(-1,0), (0,-1)]
        
        steps = [n, n-1, n-1, n-2]
        
        m = [[0] *n for i in range(n)]
        
        dindex = 0
        x, y = -1, 0
        moves = 0
        for i in range(1, n*n+1):
            dx, dy = dirs[dindex]
            x, y = x+dx, y+ dy
            m[y][x] = i
            moves += 1
            if moves == steps[dindex]:
                moves = 0
                dindex = (dindex+1)%4
                if dindex==0:
                    steps =[step-2 for step in steps]
        return m
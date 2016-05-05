class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        N = len(dungeon)
        M = len(dungeon[0])
        matrix = []
        for i in range(N):
            row = [0]*M
            matrix.append(row)
        matrix[N-1][M-1] = 1 if dungeon[N-1][M-1]>=0 else -dungeon[N-1][M-1]+1
        for n in range(M+N-1, -1, -1):
            for x in range(N):
                y = n-x
                if y <0 or y>=M:
                    continue
                candidates=[]
                if x+1<N:
                    candidates.append(matrix[x+1][y])
                if y+1<M:
                    candidates.append(matrix[x][y+1])
                if not candidates: continue
                min_need = min(candidates)
                if dungeon[x][y]>=0:
                    if dungeon[x][y]>=min_need:
                        matrix[x][y]=1
                    else:
                        matrix[x][y]=min_need-dungeon[x][y]
                else:
                    matrix[x][y] = min_need-dungeon[x][y]
        return matrix[0][0]
            

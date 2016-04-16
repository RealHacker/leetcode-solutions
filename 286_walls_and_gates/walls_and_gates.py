class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = []
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    q.append((i, j, 0))
        while q:
            i, j, d = q.pop(0)
            if i>0 and rooms[i-1][j]>d+1:
                rooms[i-1][j]=d+1
                q.append((i-1, j, d+1))
            if j>0 and rooms[i][j-1]>d+1:
                rooms[i][j-1] = d+1
                q.append((i, j-1, d+1))
            if i<len(rooms)-1 and rooms[i+1][j]>d+1:
                rooms[i+1][j] = d+1
                q.append((i+1, j, d+1))
            if j<len(rooms[0])-1 and rooms[i][j+1]>d+1:
                rooms[i][j+1] = d+1
                q.append((i, j+1, d+1))
        return
            

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        islands = 0
        islandno = 1
        matrix =[[0 for j in range(n)] for i in range(m)]
        imap = {}
        
        result = []
        for x, y in positions:
            ajacent_islands = set()
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                if x+dx >= 0 and x+dx<m and y+dy>=0 and y+dy<n and matrix[x+dx][y+dy]>0:
                    ajacent_islands.add(matrix[x+dx][y+dy])
            if not ajacent_islands:
                matrix[x][y] = islandno
                imap[islandno]=islandno
                islandno += 1
                islands += 1
            else:
                temp = set()
                for island in ajacent_islands:
                    while imap[island]!=island:
                        island = imap[island]
                    temp.add(island)
                leader = temp.pop()
                matrix[x][y]=leader
                for island in temp:
                    imap[island] = leader
                    islands -= 1
            result.append(islands)
        return result
                
                    

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # build trie
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["$"]=word
        
        # DFS from each cell in board
        self.board = board
        self.result = set()
        self.visited = []
        self.reset_visited()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, self.trie)
        
        return list(self.result)
        
    def reset_visited(self):
        self.visited = []
        for i in range(len(self.board)):
            row = []
            for j in range(len(self.board[0])):
                row.append(False)
            self.visited.append(row)
            
    def dfs(self, x, y, node):
        c = self.board[x][y]
        if c not in node:
            return
        
        node = node[c]
        if "$" in node:
            self.result.add(node['$'])
            
        self.visited[x][y] = True
        for dx, dy in [(0,1),(1,0), (-1,0), (0,-1)]:
            if 0<=x+dx<len(self.board) and 0<=y+dy<len(self.board[0]) and not self.visited[x+dx][y+dy]:
                self.dfs(x+dx, y+dy, node)
        self.visited[x][y]=False
                
        

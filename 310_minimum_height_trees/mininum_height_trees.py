class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n==1:
            return [0]
        self.aj = {}
        for edge in edges:
            self.aj.setdefault(edge[0], []).append(edge[1])
            self.aj.setdefault(edge[1], []).append(edge[0])
        _, nodes1 = self.bfs(-1, 0)
        l, nodes2 = self.bfs(-1, nodes1[-1])
        if l%2:
            return [nodes2[l/2]]
        else:
            return [nodes2[l/2-1], nodes2[l/2]]
            
    def bfs(self, v0, v):
        if v0 !=-1 and len(self.aj[v])==1:
            return 1, [v]
        else:
            l = -1
            nodes = []
            for node in self.aj[v]:
                if node == v0: continue
                ll, nn = self.bfs(v, node)
                if ll+1 > l:
                    l = ll + 1
                    nodes = [v] + nn
            return l, nodes
            

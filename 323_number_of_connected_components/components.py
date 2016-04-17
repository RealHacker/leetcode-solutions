from collections import defaultdict

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if n==0:
            return 0
        if not edges:
            return n
        # First convert the edge list to a map
        edge_map = defaultdict(list)
        for x, y in edges:
            edge_map[x].append(y)
            edge_map[y].append(x)
        
        components = 0
        left = set(range(n))
        while left:
            components+=1
            q = [left.pop()]
            while q:
                v = q.pop(0)
                for vv in edge_map[v]:
                    if vv in left:
                        q.append(vv)
                        left.remove(vv)
                    
        return components
            

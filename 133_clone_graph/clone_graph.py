# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import copy
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        self.visited = {}
        newnode = self.traverse(node)
        return newnode
        
    def traverse(self, node):
        if not node:
            return None
        if node.label in self.visited:
            return self.visited[node.label]
        newnode = copy.copy(node)
        self.visited[node.label] = newnode
        
        newnode.neighbors = []
        for neighbor in node.neighbors:
            new_neighbor = self.traverse(neighbor)
            newnode.neighbors.append(new_neighbor)
        
        return newnode

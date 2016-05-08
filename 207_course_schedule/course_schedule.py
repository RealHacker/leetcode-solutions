class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
    	# try to do topological sort, if cannot finish, there is a loop
    	in_edges = {}
    	out_edges = {}
    	nodes = []
    	for i in range(numCourses):
    		nodes.append(i)
    		in_edges[i] = []
    		out_edges[i] = []
    	for s,t in prerequisites:
    		out_edges[s].append(t)
    		in_edges[t].append(s)
    	while True:
    		found = False
    		for i in nodes:
    			if not in_edges[i]:
    				found = True
    				nodes.remove(i)
    				for node in out_edges[i]:
    					in_edges[node].remove(i)
    		if not found:
    			break
    	return not nodes
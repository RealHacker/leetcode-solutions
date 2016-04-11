class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n==1: return True
        self.leaders = {}
        self.groups = {}
        for i, j in edges:
            if i>j: 
                i, j = j, i
            if i in self.leaders:
                if j in self.leaders:
                    if self.leaders[i]==self.leaders[j]:
                        return False
                    else:
                        leaderi = self.leaders[i]
                        leaderj = self.leaders[j]
                        if leaderi>leaderj:
                            leaderi, leaderj = leaderj, leaderi
                        groupi = self.groups[leaderi]
                        groupj = self.groups[leaderj]
                        self.groups[leaderi] = groupi|groupj
                        for item in groupj:
                            self.leaders[item]=leaderi
                        del self.groups[leaderj]
                else:
                    self.leaders[j]=self.leaders[i]
                    self.groups[self.leaders[i]].add(j)
            else:
                if j not in self.leaders:
                    self.leaders[j] = i
                    self.leaders[i] = i
                    self.groups[i] = set([i, j])
                else:
                    if i>self.leaders[j]:
                        self.leaders[i]=self.leaders[j]
                        self.groups[self.leaders[j]].add(i)
                    else:
                        group = self.groups[self.leaders[j]]
                        group.add(i)
                        self.groups[i] = group
                        del self.groups[self.leaders[j]]
                        for item in group:
                            self.leaders[item]=i
            # print "leaders:%s"%self.leaders
            # print self.groups
        return len(self.groups)==1 and len(self.groups[0])==n
                    
            

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticketmap = {}
        self.tickets = tickets
        for f,t in tickets:
            if f not in ticketmap:
                ticketmap[f] = [t]
            else:
                ticketmap[f].append(t)
        for k, v in ticketmap.items():
            v.sort()
        
        return self.recurse(ticketmap, 'JFK', ['JFK'])
        
    def recurse(self, tmap, start, it):
        if len(it)==len(self.tickets)+1:
            return it
        if start not in tmap or not tmap[start]:
            return None
        for i, next in enumerate(tmap[start]):
            del tmap[start][i]
            r = self.recurse(tmap, next, it[:]+[next])
            if r:
                return r
            else:
                tmap[start].insert(i, next)
        return None

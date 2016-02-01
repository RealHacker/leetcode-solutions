from collections import defaultdict

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print s, p
        pmap =defaultdict(int)
        for c in p:
            if c=="*":continue
            pmap[c]+=1
        smap =defaultdict(int)
        self.cpos = defaultdict(list)
        for i,c in enumerate(s):
            smap[c]+=1
            self.cpos[c].append(i-len(s))
        return self.recurse(s, p, smap, pmap)
        
            
    def recurse(self, s,p, smap, pmap):
        if not p:return not s
        if p=="*":return True
        if p=="?":
            if len(s)==1: return True
            else: return False
        if p==s:return True
        
        if p[0]=="?":
            if not s: return False
            smap = smap.copy()
            smap[s[0]]-=1
            pmap = pmap.copy()
            pmap["?"]-=1
            return self.recurse(s[1:], p[1:], smap, pmap)
        elif p[0]=="*":
            for key in smap:
                if smap[key]<pmap[key]:
                    return False
            
            found = False
            qs = 0
            for i,c in enumerate(p):
                if c=="?":
                  qs+=1  
                if c not in "?*":
                    found = True
                    break
            
            if found:
                points = map(lambda n:n+len(s), filter(lambda x:x+len(s)>=0, self.cpos[c]))
            else:
                i=len(p)
                points = [len(s)]
                
            for point in points:
                if point>=qs:
                    smap = smap.copy()
                    for chr in s[:point]:
                        smap[chr]-=1
                    pmap = pmap.copy()
                    pmap["?"]-=qs
                    if self.recurse(s[point:], p[i:], smap, pmap):
                        return True
            return False
        else:
            if not s: return False
            if p[0]!=s[0]: return False
            
            smap = smap.copy()
            smap[s[0]]-=1
            pmap = pmap.copy()
            pmap[s[0]]-=1
            return self.recurse(s[1:], p[1:], smap, pmap)
            
                

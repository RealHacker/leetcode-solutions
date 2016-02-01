class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        perms =[]
        for perm in itertools.permutations(range(n)):
            diag = set()
            tdiag = set()
            conflict = False
            for i, c in enumerate(perm):
                d = i+c
                td = i+n-c
                if d in diag or td in tdiag:
                    conflict = True
                    break
                diag.add(d)
                tdiag.add(td)
            if not conflict:
                perms.append(perm)
        def convert(p):
            ret = []
            for c in perm:
                s = ""
                for i in range(n):
                    if i!=c:
                        s+="."
                    else:
                        s+="Q"
                ret.append(s)
            return ret
        return [convert(perm) for perm in perms]
            
                
        

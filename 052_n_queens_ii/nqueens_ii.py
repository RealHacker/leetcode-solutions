class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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
        return len(perms)
            
                
        

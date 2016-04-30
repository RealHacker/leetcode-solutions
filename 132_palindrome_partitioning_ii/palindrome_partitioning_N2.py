class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        odddict = {}
        evendict = {}
        # map from (i,j) -> whether s[i:j] is palindrome
        
        for i in range(len(s)):
            # find the even length palindrome
            ii = i-1
            jj = i
            cnt = 0
            while ii>=0 and jj<len(s) and s[ii]==s[jj]:
                ii-=1
                jj+=1
                cnt += 1
            evendict[i] = cnt
            # find the odd length
            ii = i-1
            jj = i+1
            cnt = 1
            while ii>=0 and jj<len(s) and s[ii]==s[jj]:
                ii -= 1
                jj += 1 
                cnt += 1
            odddict[i] = cnt
        
        # DP part
        table = [-1]
        for i in range(1, len(s)+1):
            _min = sys.maxint
            for j in range(i):
                passed = False
                if (i-j)%2==0 and evendict[(i+j)/2]>=(i-j)/2:
                    passed = True
                if (i-j)%2!=0 and odddict[(i+j)/2]>=(i-j)/2+1:
                    passed = True
                if passed and table[j]!=sys.maxint:
                    _min = min(_min, table[j]+1)
            table.append(_min)
        return table[-1]
        
                    

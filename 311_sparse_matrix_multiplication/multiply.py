class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B: return []
        ra = len(A)
        la = len(A[0])
        rb = len(B)
        lb = len(B[0])
        
        b_status = [any([B[i][j] for i in range(rb)]) for j in range(lb)]
        result = []
        for i in range(ra):
            if not any(A[i]):
                result.append([0]*lb)
            else:
                temp = []
                for j in range(lb):
                    if not b_status:
                        temp.append(0)
                    else:
                        temp.append(sum([A[i][x]*B[x][j] for x in range(la)]))
                result.append(temp)
        return result

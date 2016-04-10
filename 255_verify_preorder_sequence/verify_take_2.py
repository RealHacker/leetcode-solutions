class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if len(preorder)<2:
            return True
        roots = [] # contains tuples (node, direction) where direction 0 for left and 1 for right
        current = preorder[0]
        for num in preorder[1:]:
            if num < current:
                for i in range(len(roots)-1, -1, -1):
                    val, dir = roots[i]
                    if dir==1: # right branch
                        if num < val: 
                            return False
                        else:
                            break
                roots.append((current, 0))
                current = num
            else:
                top = -1
                for i in range(len(roots)-1, -1, -1):
                    val, dir = roots[i]
                    if dir==0:
                        if num < val:
                            break
                        else:
                            top = i
                if top < 0:
                    roots.append((current, 1))
                else:
                    del roots[top+1:]
                    roots[top] = (roots[top][0], 1)
                current = num
        return True
                    

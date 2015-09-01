class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # build a list of tuples (char, number)
        patterns = []
        i = 0
        while i<len(p):
            if p[i]==".":
                _id = "dot"
            else:
                _id = p[i]
            if i+1<len(p) and p[i+1]=="*":
                patterns.append((_id, -1))
                i+=2
            else:
                patterns.append((_id, 1))
                i+=1

        #print patterns
        # shrink the patterns
        i = len(patterns)-1
        while i>0:
            p = patterns[i]
            last = patterns[i-1]
            if p[0]==last[0] and p[1]<0 and last[1]<0:
                del patterns[i]
            i-=1
        #print patterns 
        
        stack = [] # for backtracking (j, pos, end)
        i = 0
        j = 0
        
        def backtrack():
            jj, start, end = stack[-1]
            if start==end:
                stack.pop()
            else:
                stack[-1][2] = end-1
            return end, jj+1
                
        while True:
            print i, j

            if i>=len(s):
                if j>=len(patterns):
                    return True
                else:
                    canConsume = True
                    for k in range(j, len(patterns)):
                        if patterns[k][1]>0:
                            canConsume = False
                            break
                    if canConsume:
                        return True
                    else:
                        if not stack:
                            return False
                        i,j = backtrack()
                        continue
                    
            elif j>=len(patterns):
                if not stack:
                    return False
                i, j = backtrack()
                continue
            
            if s[i]==patterns[j][0]:
                if patterns[j][1]<0:
                    start = i
                    while i<len(s) and s[i]==patterns[j][0]:
                        i+=1
                    stack.append([j, start, i-1])
                else:
                    i+=1
            elif patterns[j][0]=="dot":
                if patterns[j][1]<0:
                    stack.append([j, i, len(s)-1])
                    i=len(s)
                else:
                    i+=1
            else:
                if patterns[j][1]>0:
                    # backtrack
                    if not stack:
                        return False
                    i,j = backtrack()
                    continue
            j+=1
            
            
                
                

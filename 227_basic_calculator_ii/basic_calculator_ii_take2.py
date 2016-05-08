class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_number(i):
            # return number, the position after number
            n = 0
            while i<len(s) and s[i] ==" ":
                i+=1
            if i==len(s):
                return None, i
            while i<len(s) and s[i] in "0123456789":
                n = n*10 + ord(s[i])-ord('0')
                i+=1
            while i<len(s) and s[i] ==" ":
                i+=1
                
            return n, i
            
        n, i = get_number(0)
        stack = [n]
        _op = None
        while i<len(s):
            if s[i] in "+-":
                op = s[i]
                if _op:
                    n1 = stack.pop()
                    n2 = stack.pop()
                    if _op =="+":
                        stack.append(n1+n2)
                    else:
                        stack.append(n2-n1)
                    _op = None
                nn, i = get_number(i+1)
                if i<len(s) and s[i] in "*/":
                    _op = op
                    stack.append(nn)
                else:
                    if op == "+":
                        stack.append(stack.pop()+nn)
                    else:
                        stack.append(stack.pop()-nn)
            else:
                op = s[i]
                nn, i = get_number(i+1)
                if op=="*":
                    stack.append(stack.pop()*nn)
                else:
                    if nn==0:
                        raise Exception("DIV_BY_ZERO")
                    stack.append(stack.pop()/nn)
        if _op:
            n1 = stack.pop()
            n2 = stack.pop()
            if _op =="+":
                stack.append(n1+n2)
            else:
                stack.append(n2-n1)
            
        return stack[0]
                
        

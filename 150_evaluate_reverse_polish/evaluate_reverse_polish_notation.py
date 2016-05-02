class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token=="+":
                    stack.append(a+b)
                elif token=="-":
                    stack.append(a-b)
                elif token=="*":
                    stack.append(a*b)
                else:
                    if a*b < 0:
                        stack.append(-(abs(a)/abs(b)))
                    else:
                        stack.append(a/b)
        return stack[0]

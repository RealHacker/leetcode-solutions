class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = []
        num = 0
        for c in input:
            if c in "+-*":
                tokens.append(num)
                num = 0
                tokens.append(c)
            else:
                num = num*10+ord(c)-ord('0')
        tokens.append(num)
        
        rset = self._recurse(tokens)
        return sorted(list(rset))
        
    def _recurse(self, tokens):
        if len(tokens)==1:
            return [tokens[0]]
        # for each operator, split
        result = []
        for i, c in enumerate(tokens):
            if isinstance(c, int): continue
            if c in "+-*":
                left = self._recurse(tokens[:i])
                right = self._recurse(tokens[i+1:])
                # get the product of 2 subparts
                for l in left:
                    for r in right:
                        if c=="+":
                            result.append(l+r)
                        elif c=="-":
                            result.append(l-r)
                        else:
                            result.append(l*r)
        return result

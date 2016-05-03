class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator==0:
            raise Exception("Div by Zero")
        if numerator==0:
            return "0"
        neg = (numerator<0) and (denominator>0) or (numerator>0) and (denominator<0)
        
        n = abs(numerator)
        d = abs(denominator)
        
        if n%d==0:
            result = str(n/d)
        else:
            result = str(n/d)+"."
            n = n%d
            digits = []
            visited = {n:0}
            loop_from = -1
            while True:
                n = n*10
                digit = n/d
                n = n%d
                
                if n in visited:
                    digits.append(digit)
                    loop_from = visited[n]
                    break
                else:
                    digits.append(digit)
                    visited[n] = len(digits)
                    
                if n==0:
                    break
            print digits
            if loop_from<0:
                suffix = ''.join([str(d) for d in digits])
            else:
                first = ''.join([str(d) for d in digits[:loop_from]])
                second = "("+''.join([str(d) for d in digits[loop_from:]])+")"
                suffix = first+second
            result += suffix
            
        if neg:
            return "-"+result
        return result

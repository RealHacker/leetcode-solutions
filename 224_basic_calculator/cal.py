class Solution(object):
    def get_token(self,s,i):
        while i<len(s) and s[i]==" ":
            i+=1
        if i>=len(s):
            return len(s), None
        if s[i] in "+-()":
            return i+1, s[i]
        num = 0
        while i<len(s) and s[i] in "0123456789":
            num = num*10+ord(s[i])-ord("0")
            i+=1
        return i, num
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        _, result = self._calculate(s, 0)
        return result
        
    def _calculate(self, s, i):
        result = 0
        while True:
            i, token = self.get_token(s, i)
            if token is None:
                break
            if token==")":
                break
            
            if isinstance(token, int):
                result = token
            elif token in "+-":
                i, _token = self.get_token(s, i)
                if _token=="(":
                    i, number = self._calculate(s, i)
                else:
                    number = _token
                if token=="+":
                    result += number
                else:
                    result -= number
            elif token=="(":
                i, result = self._calculate(s, i)

                    
        return i, result      
                

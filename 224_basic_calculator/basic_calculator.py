import string
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        self.s = s
        self.idx = 0
        return self.eval()
    
    def eval(self):
        current = 0
        def getNumber():
            n = 0
            while self.idx < len(self.s) and self.s[self.idx] in string.digits:
                n = n*10 + int(self.s[self.idx])
                self.idx += 1
            print "Number %d"%n
            return n
        while self.idx<len(self.s):
            if self.s[self.idx] == " ":
                self.idx += 1
            elif self.s[self.idx] in string.digits:
                current = getNumber()
            elif self.s[self.idx] == "+":
                self.idx += 1
                while self.s[self.idx]==" ":
                    self.idx += 1
                if self.s[self.idx] in string.digits:
                    current += getNumber()
                elif self.s[self.idx] == "(":
                    self.idx +=1 
                    current += self.eval()
            elif self.s[self.idx] == "-":
                self.idx += 1
                while self.s[self.idx]==" ":
                    self.idx += 1
                if self.s[self.idx] in string.digits:
                    current -= getNumber()
                elif self.s[self.idx] == "(":
                    self.idx += 1 
                    current -= self.eval()
            elif self.s[self.idx] == "(":
                self.idx += 1
                current = self.eval()
            elif self.s[self.idx] == ")":
                self.idx += 1
                return current
        print "expression %d"%current
        return current


print Solution().calculate("1+2 - ( 3 + (2)- 2)+ 3")

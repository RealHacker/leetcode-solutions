class Solution:
    # @param {string} s
    # @return {integer}
    def listfind(self, l, element):
        try:
            idx = l.index(element)
        except:
            idx = -1
        return idx
        
    def calculate(self, s):
        components = []
        num = -1
        for c in s:
            if c == ' ':
                continue
            if c in '+-*/':
                if num >= 0:
                    components.append(num)
                    num = -1
                components.append(c)
            
            if c in string.digits:
                if num < 0:
                    num = int(c)
                else:
                    num = num *10 + int(c)
        if num >= 0:
            components.append(num)
        
        idx = 0    
        while True:
            if idx >= len(components):
                break
            if components[idx] == '*':
                components[idx-1:idx+2]=[components[idx-1]*components[idx+1]]
                continue
            if components[idx] == '/':
                components[idx-1:idx+2]=[components[idx-1]/components[idx+1]]
                continue
            else:
                idx = idx+1
            
        
        idx = 0    
        while True:
            if idx >= len(components):
                break
            if components[idx] == '+':
                components[idx-1:idx+2]=[components[idx-1]+components[idx+1]]
                continue
            if components[idx] == '-':
                components[idx-1:idx+2]=[components[idx-1]-components[idx+1]]
                continue
            else:
                idx = idx+1
                
        return components[0]
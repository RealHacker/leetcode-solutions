class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.recurse(num, [])
        
    def recurse(self, num, triples):
        if not num :
            return len(triples)>=3

        if not triples or len(triples)==1:
            if num[0]=='0':
                _triples = triples+[0]
                return self.recurse(num[1:], _triples)
            for i in range(1, len(num)/2+1):
                _triples = triples + [int(num[:i])]
                if self.recurse(num[i:], _triples):
                    return True
            return False
            
        if num[0]=='0':
            return False
        if len(triples)>=2:
            target = triples[-1]+triples[-2]
            if num.startswith(str(target)):
                _triples = triples + [target]
                return self.recurse(num[len(str(target)):], _triples)
            else:
                return False
                    
            

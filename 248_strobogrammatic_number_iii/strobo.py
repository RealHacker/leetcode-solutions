class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        if int(low)>int(high):return 0
        h = self.countLessThan(int(high))
        l = self.countLessThan(int(low))
        print l, h
        result = h-l
        if self.isStrobogrammatic(high):
            result+=1
        return result
    
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        pairs = {"1":"1","0":"0", "8":"8", "6":"9","9":"6"}
        if len(num)%2==0:
            half = len(num)/2
        else:
            half = len(num)/2+1
        for i in range(half):
            if num[i] not in pairs:
                return False
            if pairs[num[i]]!=num[len(num)-1-i]:
                return False
        return True
    
    def strobolize(self, digits):
        pairs = {"1":"1","0":"0", "8":"8", "6":"9","9":"6"}
        return ''.join(reversed([pairs[d] for d in digits]))
        
    def countLessThan(self, n):
        strobos = [0, 1, 6, 8, 9]
        # first handle the edge case of single digits
        if n<=10:
            return len(filter(lambda x:x<n and x!=6 and x!=9, strobos))
        
        total = 0
        s = str(n)
        # all numbers with less digits than s are ok
        for i in range(1, len(s)):
            total += self.numbersWithDigits(i)
            print total
            
        # numbers with exactly len(s) digits
        if len(s)%2==0:
            half = len(s)/2
        else:
            half = len(s)/2+1
        l = len(s)
        for i in range(half):
            digit = int(s[i])
            if i==0:
                first_candidates = len(filter(lambda x:x<digit and x!=0, strobos))
            else:
                if len(s)%2 and i==half-1:
                    first_candidates = len(filter(lambda x:x<digit, [0, 1, 8]))
                else:
                    first_candidates = len(filter(lambda x:x<digit, strobos))
            l-=2
            total += first_candidates * self.sequencesWithDigits(l)
            if digit not in strobos: break
            if len(s)%2 and i==half-1 and digit not in [0,1,8]: break
        else:
            # whether the strobo number with same first half is less than n
            ss = s[:half] + self.strobolize(s[:half]) if len(s)%2==0 else s[:half] + self.strobolize(s[:half-1])
            if int(ss)<n:
                total += 1

        return total
                
    def numbersWithDigits(self, n):
        if n<2: 
            return self.sequencesWithDigits(n)
        else:
            return 4*self.sequencesWithDigits(n-2) # prepend 1689
            
    def sequencesWithDigits(self, n):
        if n<=0:
            return 1
        elif n==1:
            return 3 # 0/1/8
        else:
            return 5*self.sequencesWithDigits(n-2) # prepend 01689

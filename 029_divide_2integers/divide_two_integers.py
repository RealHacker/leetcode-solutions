class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        result = 0
        
        negative = False
        if dividend > 0 and divisor < 0:
            divisor = -divisor
            negative = True
        if dividend <0 and divisor>0:
            dividend = -dividend
            negative = True
        if dividend <0 and divisor<0:
            dividend = -dividend
            divisor = -divisor
            
        # x2 until it is larger than dividend
        d = divisor
        n = 0
        while d < dividend:
            n += 1
            d = d<<1
        # if has shifted, shift back once
        if n > 0:
            d = d>>1
            n -= 1
        print d, n
        
        while n>0:
            if dividend>=d:
                dividend -= d
                result += 1<<n
            d = d>>1
            n -= 1
            
        while dividend>=divisor:
            dividend -= divisor
            result += 1
        
        if negative:
            result = -result
        if result>=(1<<31):
            result = (1<<31)-1
        if result<-(1<<31):
            result = -(1<<31)
            
        return result

print Solution().divide(2147483647, 3)

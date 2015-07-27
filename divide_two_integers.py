class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        i = 0
        sign = 1
        if dividend >0 and divisor<0:
            divisor = -divisor
            sign = -1
        if dividend <0 and divisor>0:
            dividend = -dividend
            sign = -1
        if dividend <0 and divisor<0:
            dividend = -dividend
            divisor = -divisor
        
        d = divisor
        n = 0
        while d < dividend:
            n += 1
            d = divisor<<n
            
        if n > 0:
            d = d>>1
            n = n-1
        while n>0:
            dividend -= d
            d = d>>1
            i += 1<<n
            n -= 1
            
        while dividend>=divisor:
            dividend -= divisor
            i+=1
        
        if sign <0:
            i = -i
        if i>=(1<<31):
            i = (1<<31)-1
        if i<-(1<<31):
            i = -(1<<31)
            
        
        return i
        
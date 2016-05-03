class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):    	
    	n = numerator
    	d = denominator
    	if n*d <0:
    		negative = True
    	else:
    		negative = False
    	n,d = abs(n), abs(d)
    	if n>=d:
    		int_part = n/d
    		n = n%d
    	else:
    		int_part = 0
    	if n==0:
    		point = False
    	else:
    		point = True
    	digits = []
    	loop_start = -1
    	if point:    	
    		idx = 0
    		appeared = {n:0}
    		
    		while n:
    			m = n*10/d
    			n = n*10%d
    			digits.append(m)
    			if n in appeared:
    				loop_start = appeared[n]
    				break
    			appeared[n] = idx+1
    			idx += 1

    	after_point = ""
    	for i, digit in enumerate(digits):
    		if i==loop_start:
    			after_point+="("
    		after_point+=str(digit)
    	if loop_start>=0:
    		after_point+=")"
	
	if not point:
		ret =  str(int_part)
	else:
		ret =  str(int_part)+"."+after_point
	if negative:
		return "-"+ret
	else:
		return ret



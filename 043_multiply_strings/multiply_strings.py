class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0]=='0' or num2[0]=='0':
            return "0"
        digits = []
        for i, c in enumerate(reversed(num1)):
            carry = 0
            temp = []
            if c=='0': continue
            for cc in reversed(num2):
                n = int(cc)*int(c)+carry
                n, carry = n%10, n/10
          	temp.append(n)
#		print temp, carry
            if carry:
                temp.append(carry)
            if not digits:
		digits.extend([0]*i)
                digits.extend(temp)
	    else:
           	carry = 0
            	for k in range(len(temp)):
                	if i+k < len(digits):
                    		current = digits[i+k]+temp[k]+carry
	                   	d, carry = current%10, current/10
	                	digits[i+k]=d
                	else:
                    		current = temp[k]+carry
                    		d, carry = current%10, current/10
                    		digits.append(d)
            	if carry:
                	digits.append(carry)
            
        result = ''.join([str(c) for c in reversed(digits)])
        return result
                    
                
                
            

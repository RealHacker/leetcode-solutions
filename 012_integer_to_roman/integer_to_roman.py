class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        bases = (('I',1),
            ('V',5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),)
        bases = bases[::-1]
        roman = ""
        while num:
            for b in bases:
                if num>=b[1]:
                  n = num/b[1]
                  num = num%b[1]
                  if n==4:
                      if b[0]=='C':
                          if roman and roman[-1]=='D':
                              roman = roman[:-1]+'CM'
                          else:
                              roman = roman+'CD'
                      if b[0]=='X':
                          if roman and roman[-1]=='L':
                              roman = roman[:-1]+'XC'
                          else:
                              roman = roman+'XL'
                      if b[0]=='I':
                          if roman and roman[-1]=='V':
                              roman = roman[:-1]+'IX'
                          else:
                              roman = roman+'IV'
                  else:
                      roman = roman + b[0]*n
                  break
        return roman
        

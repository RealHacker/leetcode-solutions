class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if " " in s:
            return False
        if s.startswith('0') or s.lower().startswith('0b'):
            try:
                int(s, 2)
            except:
                pass
            else:
                return True
        if s.startswith('0'):
            try:
               int(s, 8)
            except:
                pass
            else:
                return True 
        if s.lower().startswith('0x'):
            try:
               int(s, 16)
            except:
                pass
            else:
                return True
        try:
           int(s, 10)
        except:
            pass
        else:
            return True
        try:
            float(s)
        except:
            pass
        else:
            return True
            
        return False

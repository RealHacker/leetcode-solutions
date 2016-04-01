# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.tmp = []
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        readcnt = 0
        if self.tmp:
            if n <= len(self.tmp):
                for i in range(n):
                    buf[i+idx] = self.tmp[i]
                del self.tmp[:n]
                return n
            else:
                readcnt += len(self.tmp)
                for c in self.tmp:
                    buf[idx]= c
                    idx+=1
                self.tmp = []
        buff = [None, None, None, None]
        while True:
            nn = read4(buff)
            if nn==0: break
            if readcnt+nn>n:
                for i in range(n-readcnt):
                    buf[idx]=buff[i]
                    idx+=1
                for i in range(n-readcnt, nn):
                    self.tmp.append(buff[i])
                return n
            else:
                readcnt+=nn
                
                for cc in buff:
                    buf[idx]=cc
                    idx+=1
                if readcnt==n:
                    break
        return readcnt
                

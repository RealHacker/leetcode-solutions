# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        readcnt = 0
        while True:
            buff = [None, None, None, None]
            c = read4(buff)
            print buff
            if c==0:
                break
            if readcnt+c>=n:
                for i in range(readcnt, n):
                    buf[i] = buff[i-readcnt]
                #print buf
                readcnt = n
                break
            for i in range(readcnt, readcnt+c):
                buf[i] = buff[i-readcnt]
            readcnt+=c
        return readcnt
                
            

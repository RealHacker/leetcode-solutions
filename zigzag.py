from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows==1:
            return s
        lines = defaultdict(str)
        down = True
        for i,c in enumerate(s):
            rem = i%(numRows+numRows-2)
            if rem < numRows:
                lines[rem]+=c
            else:
                lineno = numRows*2-2-rem
                lines[lineno] += c
        ss="".join([lines[i] for i in range(numRows)])
        
        return ss

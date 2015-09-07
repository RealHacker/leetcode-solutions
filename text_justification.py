class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        i = 0
        while i<len(words):
            llen = 0  
            cur = i
            while i<len(words):
                llen += len(words[i])
                if llen>maxWidth:
                    llen -= len(words[i])
                    break
                llen+=1
                i+=1
            
            llen -=1 # back one extra space
            if i != len(words):
                wordcnt = i-cur
                extra = maxWidth-llen                 
                if wordcnt>1:
                    spaces = extra/(wordcnt-1)
                    r = extra%(wordcnt-1)
                else:
                    spaces = extra
                    r = 0
            else:
                spaces = 0
                r = 0
            #print spaces, r
            line = ""
            for word in words[cur:i]:
                line += word
                line += " "*(spaces+1)
                if r>0:
                    line += " "
                    r -= 1
            
            line = line[:maxWidth]
            if len(line)<maxWidth:
                line+=" "*(maxWidth-len(line))

            lines.append(line)
        
        return lines
            

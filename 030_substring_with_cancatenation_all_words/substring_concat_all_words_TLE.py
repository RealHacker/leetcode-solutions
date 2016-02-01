class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        wlen = len(words[0])
        # first build the word counter
        counter = {}
        for word in words:
            counter[word] = 1 if word not in counter else counter[word]+1
        print counter
            
        def allWordsFound(d):
            for key in d:
                if d[key]>0:
                    return False
            return True
        i = 0
        result = []
        for start in range(wlen):
            #print "starting at %d"%start
            d = {k:v for k, v in counter.items()}
            cursor = start
            while True:
                i+=1
                #print "cursor at %d,%d"%(start, cursor)
                if allWordsFound(d):
                   result.append(start)
                if cursor>=len(s):
                    break
                current = s[cursor:cursor+wlen]
                if current in d:
                    if d[current]>0:
                        d[current]-=1
                        cursor += wlen
                    else:
                        first = s[start:start+wlen]
                        d[first]+=1
                        start += wlen
                else:
                    start = cursor + wlen
                    cursor = start
                    d = {k:v for k, v in counter.items()}
        print i
        return result
                    

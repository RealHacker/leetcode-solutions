import copy
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.memo = {}
        self.s = s
        self.buildMemo(4, 0)
        splits = self.memo[(4,0)]
        result = []
        for split in splits:
            ss = ""
            left = 0
            print split
            for i in split:
                ss += s[left:i]+"."
                left = i
            ss += s[i:]
            result.append(ss)
        print result
        return result
        
    def buildMemo(self, segment, start):
        if (segment, start) in self.memo:
            return
        if segment <= 0:
            return
        if segment == 1:
            if start < len(self.s)-3 or start==len(self.s) or int(self.s[start:])>255 or (self.s[start]=='0' and start!=len(self.s)-1):
                return
            self.memo[(1, start)] = [[start]]
        else:
            if (segment, start) not in self.memo:
               temp = self.memo[(segment, start)] = []
                        
            if start+1<len(self.s):
                self.buildMemo(segment-1, start+1)
                if (segment-1, start+1) in self.memo:
                    ll = copy.deepcopy(self.memo[(segment-1, start+1)])
                    if start != 0:
                        for l in ll:
                            l.insert(0, start)
                    self.memo[(segment, start)].extend(ll)
            
            if start+2<len(self.s):
                self.buildMemo(segment-1, start+2)
                if self.s[start]!='0' and (segment-1, start+2) in self.memo:
                    ll = copy.deepcopy(self.memo[(segment-1, start+2)])
                    if start != 0:
                        for l in ll:
                            l.insert(0, start)
                    self.memo[(segment, start)].extend(ll)
                
            if start+3<len(self.s):
                self.buildMemo(segment-1, start+3)
                if self.s[start]!='0' and int(self.s[start:start+3])<256 and (segment-1, start+3) in self.memo:
                    ll = copy.deepcopy(self.memo[(segment-1, start+3)])
                    if start != 0:
                        for l in ll:
                            l.insert(0, start)
                    self.memo[(segment, start)].extend(ll)
        

Solution().restoreIpAddresses("0000")
Solution().restoreIpAddresses("19216800")

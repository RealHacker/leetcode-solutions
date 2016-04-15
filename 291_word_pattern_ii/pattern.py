from collections import defaultdict
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern:
            return not str
        if not str:
            return not pattern
            
        times = defaultdict(int)
        for c in pattern:
            times[c] += 1
        
        slen = len(str)
        times_list = times.items()
        combs = self.get_combinations(times_list, slen)
        
        for comb in combs:
            dct = {}
            idx = 0
            for c in pattern:
                if c not in dct:
                    dct[c]= str[idx:idx+comb[c]]
                else:
                    if dct[c]!=str[idx:idx+comb[c]]:
                        break
                idx += comb[c]
            else:
                if len(dct)!=len(set(dct.values())):
                    continue
                return True
        return False
            
            
    def get_combinations(self, times_list, slen):
        # times_list is like [(c, cnt), (c2, cnt2), ...]
        # returns: [{c1:3, c2:2}, {}, ...]
        if len(times_list)==1:
            key, cnt = times_list[0]
            if slen%cnt!=0:
                return []
            else:
                return [{key: slen/cnt}]
        i = 1
        results = []
        while True:
            key, cnt = times_list[0]
            if i*cnt>=slen:
                break
            sub_results = self.get_combinations(times_list[1:], slen-i*cnt)
            for d in sub_results:
                d.update({key: i})
                results.append(d)
            i += 1
        return results
            
                
            

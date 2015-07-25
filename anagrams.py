from collections import defaultdict
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dic = defaultdict(list)
        for s in strs:
            d = defaultdict(int)
            for c in s:
                d[c]+=1
            keystr = ''.join([k+str(d[k]) for k in sorted(d.keys)])
            dic[keystr].append(s)
        result = []
        for k, v in dic.items:
            result.append(' '.join(v))
        return result

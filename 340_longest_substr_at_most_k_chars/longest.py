from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k==0: return 0
        positions = defaultdict(list)
        charset = set()
        
        _maxlen = 0
        _start = -1
        for i, c in enumerate(s):
            charset.add(c)
            if len(charset)>k:
                first_to_finish = i
                char_to_delete = ""
                for key in positions:
                    if positions[key][-1] <first_to_finish:
                        first_to_finish = positions[key][-1]
                        char_to_delete = key
                _start = first_to_finish
                del positions[char_to_delete]
                charset.remove(char_to_delete)
            positions[c].append(i)
            
            if i-_start>_maxlen:
                _maxlen = i-_start
                
        return _maxlen
        
            
            

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        d = {}
        for i,c in enumerate(pattern):
            if c not in d:
                d[c] = words[i]
            else:
                if d[c]!= words[i]:
                    return False
        values = set()
        for k in d:
            if d[k] in values:
                return False
            values.add(d[k])
        return True
        

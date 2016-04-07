import string
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = []
        alphabet = string.lowercase
        for s in strings:
            if not groups:
                groups.append([s])
                continue
            found = False
            for group in groups:
                if len(s)!=len(group[0]): 
                    continue
                if len(s)==1:
                    group.append(s)
                    found = True
                    break
                diff = (ord(s[0]) - ord(group[0][0]) +26)%26
                for i in range(1, len(s)):
                    if (ord(s[i]) - ord(group[0][i])+26)%26!= diff:
                        break
                else:
                    group.append(s)
                    found = True
                    break
            if not found:
                groups.append([s])
        for group in groups:
            group.sort()
        return groups

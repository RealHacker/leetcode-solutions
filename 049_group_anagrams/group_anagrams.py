class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return []

        d={}
        for s in strs:
            k="".join(sorted(s))
            if not d.has_key(k):
                d[k] = []
            d[k].append(s)
        result=[]
        for k,v in d.items():
            v.sort()
            result.append(v)
        return result

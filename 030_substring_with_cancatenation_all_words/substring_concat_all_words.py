class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dict  = collections.defaultdict(int)
        for w in words: dict[w] += 1
        l,res = len(words[0]),[]
        for i in xrange(l):
            dict1 = dict.copy()
            j = i
            while j < len(s) - l + 1:
                dict1[s[j:j+l]] -= 1
                while dict1[s[j:j+l]] < 0:
                    dict1[s[i:i+l]] += 1
                    i += l
                j += l
                if (j-i) / l == len(words) : res.append(i)
        return res

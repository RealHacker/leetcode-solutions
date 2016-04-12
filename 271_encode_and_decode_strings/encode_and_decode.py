class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        encoded = ""
        for s in strs:
            encoded += str(len(s))+"."+s
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        result = []
        while True:
            idx = s.find(".")
            if idx<0:
                break
            lenlen = int(s[0:idx])
            ss = s[idx+1:idx+1+lenlen]
            result.append(ss)
            s = s[idx+1+lenlen:]
        return result
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

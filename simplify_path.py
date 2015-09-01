class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = ""
        segments = path.split("/")
        parts = []
        for seg in segments:
            seg = seg.strip()
            if not seg or seg==".":
                continue
            if seg=="..":
                if parts:
                    parts.pop()
            else:
                parts.append(seg)
        result = "/"+"/".join(parts)
        return result
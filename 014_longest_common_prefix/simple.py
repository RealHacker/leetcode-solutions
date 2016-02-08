def longestCommonPrefix(self, strs):
    if not strs: return ''
    i = 0
    while i < len(min(strs, key = len)):
        if len({s[i] for s in strs}) != 1: break
        i += 1
    return strs[0][:i]

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = [int(digits) for digits in version1.split(".")]
        v2 = [int(digits) for digits in version2.split(".")]

        l = min(len(v1), len(v2))
        for i in range(l):
            if v1[i]!=v2[i]:
                return 1 if v1[i]>v2[i] else -1
        if len(v1)==len(v2):
            return 0
        elif len(v1)>len(v2):
            i += 1
            while i <len(v1):
                if v1[i]>0:
                    return 1
                i+=1
            return 0
        else:
            i += 1
            while i <len(v2):
                if v2[i]>0:
                    return -1
                i+=1
            return 0

print Solution().compareVersion("1.0", "1")


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        poses = []
        for i,c in enumerate(s):
            if c.lower() in vowels:
                poses.append(i)
        
        chars = [c for c in s]
        for k in range(len(poses)/2):
            chars[poses[k]], chars[poses[-k-1]] = chars[poses[-k-1]], chars[poses[k]] 
        
        return ''.join(chars)

import string

class Solution:

    # @param {string} s

    # @return {boolean}

    def isPalindrome(self, s):

        s = ''.join([c.lower() for c in s if c in string.letters+string.digits])

        if not s:

            return True

        l = len(s)

        for i in range(l/2):

            if s[i] != s[l-i-1]:

                return False

        return True

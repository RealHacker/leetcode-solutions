class Solution(object):

    def canWinNim(self, n):

        """

        :type n: int

        :rtype: bool

        """

        self.d = {}

        if n<=3:

            return True

        else:

            for k in [n-3, n-2, n-1] :

                if k not in self.d:

                    self.d[k] = self.canWinNim(k)

                if not self.d[k]:

                    return True

            return False

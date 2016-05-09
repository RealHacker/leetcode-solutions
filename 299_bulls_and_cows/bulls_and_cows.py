from collections import Counter

class Solution(object):

    def getHint(self, secret, guess):

        """

        :type secret: str

        :type guess: str

        :rtype: str

        """

        a = 0

        b = 0

        counter1 = Counter()

        counter2 = Counter()

        for i,c in enumerate(secret):

            if guess[i] == secret[i]:

                a += 1

            else:

                counter1[c]+=1

                counter2[guess[i]]+=1

        for k in counter1:

            if k in counter2:

                b+= min(counter1[k], counter2[k])

        return "%dA%dB"%(a, b)

            

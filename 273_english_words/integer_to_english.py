class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.d = {
            1000000000: "Billion",
            1000000:"Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninty",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6 :"Six",
            5:"Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
        }
        self.keys = sorted(self.d.keys(), reverse=True)
        
        if num==0:
            return "Zero"
        return self.helper(num)
        
    def helper(self, num):
        s = ""
        i = 0
        while num:
            while self.keys[i]>num:
                i+=1
            k = self.keys[i]
            if s:
                s += " "
            if k>=100:
                n = num/k
                s1 = self.helper(n)
                s += s1+" "+self.d[k]
                num = num%k
            else:
                num -= k
                s += self.d[k]
        return s

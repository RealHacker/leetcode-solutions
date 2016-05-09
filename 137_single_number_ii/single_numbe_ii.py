class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        bins = []
        maxlen = 0
        negatives = 0
        for num in nums:
            if num <0:
                negatives += 1
                num = -num
            bins.append(bin(num)[2:])
            maxlen = max(maxlen, len(bin(num))-2)
        sums = [0 for n in range(maxlen)]
        for i in range(len(bins)):
            bins[i] = '0'*(maxlen-len(bins[i]))+bins[i]
            for j in range(maxlen):
                sums[j] += int(bins[i][j])
                
        for j in range(maxlen):
            sums[j] = sums[j]%3
        negative = negatives %3
        s = ''.join([str(k) for k in sums])
        val = int(s, base=2)
        return -val if negative else val

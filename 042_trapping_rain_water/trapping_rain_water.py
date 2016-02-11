class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        peaks = []
        lefts = []
        rights = []
        for i in range(len(height)):
            if (i==0 or height[i]>height[i-1]) and (i==len(height)-1 or height[i]>=height[i+1]):
                peaks.append(i)
        max = 0
        for peak in peaks:
            if height[peak] > max:
                max = height[peak]
            lefts.append(max)
        #print lefts
        
        max = 0
        for peak in reversed(peaks):
            if height[peak]>max:
                max = height[peak]
            rights.append(max)
        rights = rights[::-1]
        #print rights
        
        for i in range(len(peaks)-1, -1, -1):
            if lefts[i]>height[peaks[i]] and rights[i]>height[peaks[i]]:
                del peaks[i]

        #print peaks
        
        water = 0
        for i in range(len(peaks)-1):
            top = min(height[peaks[i]], height[peaks[i+1]])
            for k in range(peaks[i]+1, peaks[i+1]):
                if top > height[k]:
                    water += (top-height[k])
        return water

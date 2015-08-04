class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        square1 = abs(C-A) * abs(D-B)
        square2 = abs(G-E) * abs(H-F)
        x_max1 = max(A, C)
        x_min1 = min(A, C)
        x_max2 = max(E, G)
        x_min2 = min(E, G)
        y_max1 = max(B, D)
        y_min1 = min(B, D)
        y_max2 = max(F, H)
        y_min2 = min(F, H)
        no_intersection = x_max1 < x_min2 or x_max2<x_min1 or y_max1<y_min2 or y_max2<y_min1
        if no_intersection:
            return square1 + square2
        else:
            xs = sorted([A, C, E, G])
            ys = sorted([B, D, F, H])
            intersection = (xs[2]-xs[1]) * (ys[2]-ys[1])
            return square1 + square2 - intersection
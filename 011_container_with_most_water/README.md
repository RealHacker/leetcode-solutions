It looks like the solution requires O(N*N) complexity, by selecting every pair of indices and computing the amount of water hold by the corresponding container.

But, similiar to the 2-sum problem, this can be solved with 2 pointers moving towards each other. The rule to update the pointers are:


1. Advance the pointer with the smaller height. In other words, if height[lo]<=height[hi], lo++; else, hi++. The rationale is: if we advance the pointer with larger height, we reduce the distance, but don't increase the height used for product (water = distance * height).
2. When advancing the pointer, we skip the indices with smaller height than current index. The rationale: that reduce both height and distance, producing a smaller product.

Of course, by using the 2 pointer algorithm, we skip some pairs of indices, we need to prove that those pairs can never produce the maximum product. A proof of contradiction is quite obvious. 
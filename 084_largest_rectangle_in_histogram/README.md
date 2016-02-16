Consider each position i as the right side used for the rectangle. Then the height of the rectangle is limited by the height at position i.

We will push the index i into a stack if the current height is larger than the last on stack, else, we pop indices out of stack until the top of stack has height < current height, and we push current index onto stack.

When an index is poped out of stack, we calculate the max rectangle that uses the index as right side.
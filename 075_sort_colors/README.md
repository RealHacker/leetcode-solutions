Maintain 2 cursors for the frontier of red and blue colors, starting at 0 and len(nums)-1.

Then for each color:

1. If it is red, swap it with red cursor. Advance red cursor and cursor.
2. If it is white, just advance cursor.
3. If it is blue, swap it with blue cursor, advance blue cursor. Don't advance cursor.
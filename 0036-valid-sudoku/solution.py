class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to store seen numbers for each row, column, and square
        # We use a set of tuples: (index, value)
        rows = set()
        cols = set()
        squares = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                # Create unique identifiers for each position type
                row_key = (r, val)
                col_key = (c, val)
                sq_key = (r // 3, c // 3, val)
                
                # Check if we've seen this value in this row, col, or square
                if row_key in rows or col_key in cols or sq_key in squares:
                    return False
                
                # Add to sets
                rows.add(row_key)
                cols.add(col_key)
                squares.add(sq_key)
                
        return True

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal_pairs = 0

        for row_index in range(n):
            row = grid[row_index]
            for col_index in range(n):
                column = [grid[i][col_index] for i in range(n)]
                if row == column:
                    equal_pairs += 1

        return equal_pairs

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        equal_pairs = 0

        for row_index in range(n):
            for col_index in range(n):
                # Initialize a flag to check if row matches column
                is_equal = True
                for i in range(n):
                    if grid[row_index][i] != grid[i][col_index]:
                        is_equal = False
                        break
                if is_equal:
                    equal_pairs += 1

        return equal_pairs

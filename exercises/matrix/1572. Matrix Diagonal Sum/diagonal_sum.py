class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mid = len(mat[0]) // 2
        even = len(mat) % 2 == 0

        start = 0
        end = len(mat) - 1
        d_sum = 0

        for idx, m in enumerate(mat):
            if not even and idx == mid and mat[idx][start] == mat[idx][end]:
                d_sum += mat[idx][start]
                start += 1
                end -= 1
                continue

            if start <= len(mat) - 1 and end >= 0:
                d_sum += mat[idx][start]
                d_sum += mat[idx][end]

            start += 1
            end -= 1

        return d_sum

    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        d_sum = 0

        for i in range(n):
            d_sum += mat[i][i]  # Primary diagonal
            d_sum += mat[i][n - 1 - i]  # Secondary diagonal

        # If the matrix size is odd, subtract the middle element once
        if n % 2 == 1:
            d_sum -= mat[n // 2][n // 2]

        return d_sum

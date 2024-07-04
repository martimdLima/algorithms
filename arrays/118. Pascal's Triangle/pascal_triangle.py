class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]

        pascal = [[1], [1, 1]]
        n = 2

        for n in range(2, numRows):
            k = 1
            triangle_row = [1]
            while k <= n - 1:
                triangle_row.append(factorial(n) // (factorial(k) * factorial(n - k)))
                k += 1
            triangle_row.append(1)
            pascal.append(triangle_row)
            n += 1

        return pascal

    def generate(numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]

        pascal = [[1]]

        for n in range(1, numRows):
            row = [1]  # Start with the first 1
            for k in range(1, n):
                row.append(pascal[n - 1][k - 1] + pascal[n - 1][k])
            row.append(1)  # End with the last 1
            pascal.append(row)

        return pascal

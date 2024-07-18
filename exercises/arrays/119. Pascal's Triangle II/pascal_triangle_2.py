class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        row = [1]
        for k in range(1, rowIndex):
            row.append(factorial(rowIndex) // (factorial(k) * factorial(rowIndex - k)))

        row.append(1)

        return row

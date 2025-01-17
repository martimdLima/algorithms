class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        x, y, z = 0, 1, 1

        for i in range(3, n + 1):
            result = x + y + z
            x, y, z = y, z, result

        return z

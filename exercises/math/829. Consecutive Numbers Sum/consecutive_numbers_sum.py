class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1

        sums = 1
        k = 1
        valid_num = True
        while valid_num:
            numerator = 2 * n - k * (k + 1)
            denominator = 2 * (k + 1)
            if numerator % denominator == 0:
                sums += 1
            k += 1
            valid_num = k * (k + 1) < 2 * n

        return sums

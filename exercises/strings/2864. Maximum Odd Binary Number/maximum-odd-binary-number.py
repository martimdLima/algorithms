class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_0 = s.count("0")
        count_1 = s.count("1")

        if count_1 > 1:
            result = "1" * (count_1 - 1) + "0" * count_0 + "1"
        else:
            result = "0" * count_0 + "1" * (count_1)

        return result

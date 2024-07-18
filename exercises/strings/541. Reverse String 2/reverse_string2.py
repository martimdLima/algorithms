class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        end = len(s) - 1
        char_list = list(s)

        if k > len(s):
            return "".join(list(reversed(s)))

        while start <= end:
            if start + k >= end:
                break
            char_list[start : start + k] = reversed(char_list[start : start + k])
            start += k * 2

        remainder = len(s) - start

        if remainder == 0:
            return "".join(char_list)

        if remainder < k:
            char_list[start : len(s)] = reversed(char_list[start : len(s)])
            return "".join(char_list)
        else:
            char_list[start : start + k] = reversed(char_list[start : start + k])
            return "".join(char_list)

    # Iterative approach 2
    def reverseStr(self, s: str, k: int) -> str:
        char_list = list(s)
        n = len(char_list)

        for start in range(0, n, 2 * k):
            end = min(start + k, n)
            char_list[start:end] = reversed(char_list[start:end])

        return "".join(char_list)

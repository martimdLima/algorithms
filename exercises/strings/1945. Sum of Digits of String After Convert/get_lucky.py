class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = "".join(map(str, [ord(char.lower()) - ord("a") + 1 for char in s]))
        result = 0

        while k > 0:
            res = 0
            for char in str(nums):
                res += int(char)
            result = res
            nums = str(result)
            k -= 1

        return result

    def getLucky(s: str, k: int) -> int:
        nums = "".join(str(ord(char) - ord("a") + 1) for char in s)

        result = sum(int(char) for char in nums)

        for _ in range(k - 1):
            result = sum(int(char) for char in str(result))

        return result

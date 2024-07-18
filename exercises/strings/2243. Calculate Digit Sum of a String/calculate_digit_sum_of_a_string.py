class Solution:
    def digitSum(self, s: str, k: int) -> str:
        result = ""

        while len(s) > k:
            nums = [
                sum(int(char) for char in s[i : i + k]) for i in range(0, len(s), k)
            ]
            s = "".join(map(str, nums))

        return s

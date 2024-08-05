class Solution:
    def toLowerCase(self, s: str) -> str:
        has_upper = any(c.isupper() for c in s)

        if not has_upper:
            return s

        lower = ""
        for char in s:
            if char.isupper():
                lower += char.swapcase()
                continue

            lower += char

        return lower

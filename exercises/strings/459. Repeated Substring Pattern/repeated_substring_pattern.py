class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        repeat_sub_string_pattern = s + s

        return repeat_sub_string_pattern.index(s, 1) < len(s)

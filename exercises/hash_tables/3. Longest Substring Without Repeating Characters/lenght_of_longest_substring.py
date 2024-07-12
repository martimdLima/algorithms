class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        char_set = set()
        str_length = len(s)

        for end in range(str_length):
            current_char = s[end]

            while current_char in char_set:
                char_set.remove(s[start])
                start += 1

            char_set.add(s[end])

            max_length = max(max_length, end - start + 1)
            print(char_set)
        return max_length

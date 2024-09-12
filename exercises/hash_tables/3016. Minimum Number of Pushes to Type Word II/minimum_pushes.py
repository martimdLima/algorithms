class Solution:
    def minimumPushes(self, word: str) -> int:
        # Sort characters by frequency (highest first) and alphabetically for ties
        frequency_counter = Counter(word)
        sorted_chars = sorted(frequency_counter.keys(), key=lambda char: (-frequency_counter[char], char))

        minimum_pushes = 0

        for i, char in enumerate(sorted_chars):
            element_index = i // 8

            minimum_pushes += (element_index + 1) * word.count(char)

        return minimum_pushes

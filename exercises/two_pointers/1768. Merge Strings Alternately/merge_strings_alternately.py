class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        size_1 = len(word1)
        size_2 = len(word2)

        if size_1 == 1 and size_2 == 1:
            return word1 + word2

        appended_counter = 0

        merged = ""
        for char in word1:
            merged += char + word2[appended_counter]
            appended_counter += 1

            if appended_counter == len(word2):
                break

        if appended_counter < len(word2):
            merged += word2[appended_counter : size_2 + 1]
        else:
            merged += word1[len(word2) : len(word1)]

        return merged

    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for char1, char2 in zip_longest(word1, word2, fillvalue=""):
            merged.append(char1)
            merged.append(char2)

        return "".join(merged)

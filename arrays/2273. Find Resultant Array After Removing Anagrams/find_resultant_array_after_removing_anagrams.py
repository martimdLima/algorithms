class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i <= len(words) - 1:
            if Counter(words[i - 1]) == Counter(words[i]):
                del words[i]
                i -= 1
            i += 1
        return words

    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if "".join(sorted(words[i - 1])) == "".join(sorted(words[i])):
                del words[i]
            else:
                i += 1
        return words

    def removeAnagrams(words: List[str]) -> List[str]:
        def get_char_count(word: str) -> tuple:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            return tuple(count)

        result = []
        prev_char_count = None

        for word in words:
            current_char_count = get_char_count(word)
            if current_char_count != prev_char_count:
                result.append(word)
                prev_char_count = current_char_count

        return result

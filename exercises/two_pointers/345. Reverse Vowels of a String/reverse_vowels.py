class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        str_list = list(s)
        start, end = 0, len(str_list) - 1

        while start < end:
            if str_list[start] not in vowels:
                start += 1
            elif str_list[end] not in vowels:
                end -= 1
            else:
                str_list[start], str_list[end] = str_list[end], str_list[start]
                start += 1
                end -= 1

        return "".join(str_list)

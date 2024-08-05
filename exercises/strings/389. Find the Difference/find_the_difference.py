class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t

        if len(s) == 0 and len(t) > 0:
            return t

        if len(s) > 0 and len(t) == 0:
            return s

        list_s = list(s)
        list_t = list(t)

        list_1 = list_s if len(list_s) > len(list_t) else list_t
        list_2 = list_t if len(list_s) > len(list_t) else list_s

        return list((Counter(list_1) - Counter(list_2)))[0]

    def findTheDifference(s: str, t: str) -> str:
        result = 0

        # XOR all characters in s
        for char in s:
            result ^= ord(char)

        # XOR all characters in t
        for char in t:
            result ^= ord(char)

        return chr(result)

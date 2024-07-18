class Solution:
    def isValid(self, s: str) -> bool:
        def is_opening_parentheses(char: str):
            return char == "(" or char == "[" or char == "{"

        def is_closing_parentheses(char: str):
            return char == ")" or char == "]" or char == "}"

        if len(s) == 0 or len(s) == 1:
            return False

        if len(s) == 2 and (
            is_opening_parentheses(s[0]) and is_opening_parentheses(s[1])
        ):
            return False

        stack = []

        matching_parentheses = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if is_opening_parentheses(char):
                stack.append(char)
                continue

            if (
                is_closing_parentheses(char)
                and not stack
                or stack.pop() != matching_parentheses[char]
            ):
                return False

        return not stack

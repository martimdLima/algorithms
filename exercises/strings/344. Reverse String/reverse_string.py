class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        queue = deque(s)
        s.clear()

        while queue:
            char = queue.pop()
            s.append(char)
        return s

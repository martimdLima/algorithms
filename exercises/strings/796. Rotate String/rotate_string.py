class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        counter = 0
        while counter <= len(goal) - 1:
            rotated = s[1:] + s[:1]
            if rotated == goal:
                return True
            s = rotated
            counter += 1

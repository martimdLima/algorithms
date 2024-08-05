class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for mv in moves:
            if mv == "U":
                pos[1] += 1
            elif mv == "D":
                pos[1] -= 1
            elif mv == "R":
                pos[0] += 1
            else:
                pos[0] -= 1

        return pos[0] == 0 and pos[1] == 0

    def judgeCircle(self, moves: str) -> bool:
        move_mapping = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

        pos = [0, 0]

        for mv in moves:
            delta = move_mapping[mv]
            pos[0] += delta[0]
            pos[1] += delta[1]

        return pos == [0, 0]

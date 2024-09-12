from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        colisions = []

        for i in range(0, len(asteroids)):
            current_asteroid = asteroids[i]

            if current_asteroid > 0:
                colisions.append(current_asteroid)
            else:
                while colisions and colisions[-1] > 0 and colisions[-1] < -current_asteroid:
                    colisions.pop()

                if colisions and colisions[-1] == -current_asteroid:
                    colisions.pop()
                elif not colisions or colisions[-1] < 0:
                    colisions.append(current_asteroid)

        return colisions

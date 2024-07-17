class Solution:
    def climbStairs(self, n: int) -> int:
        step_1 = 1
        step_2 = 1

        for step in range(2, n + 1):
            current_step = step_1 + step_2
            step_2 = step_1
            step_1 = current_step

        return step_1

    def climbStairs(self, n: int) -> int:
        def climb(num, step_1=1, step_2=1, step=2):
            if step > num:
                return step_1
            current_step = step_1 + step_2
            return climb(num, current_step, step_1, step + 1)

        return climb(n)

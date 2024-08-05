class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        min_val = min(salary)
        max_val = max(salary)

        for idx, sal in enumerate(salary):
            if sal == min_val or sal == max_val:
                salary.pop(idx)
                continue
        return sum(salary) / len(salary)

    def average(self, salary: List[int]) -> float:
        min_val = float("inf")
        max_val = float("-inf")
        total = 0

        for sal in salary:
            if sal < min_val:
                min_val = sal
            if sal > max_val:
                max_val = sal
            total += sal

        total -= min_val + max_val
        return total / (len(salary) - 2)

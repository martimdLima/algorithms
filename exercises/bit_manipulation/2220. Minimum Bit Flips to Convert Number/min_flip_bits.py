class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = bin(start)[2:]
        bin_goal = bin(goal)[2:]

        max_len = max(len(bin_start), len(bin_goal))

        bin_start = list(bin_start.zfill(max_len))
        bin_goal = list(bin_goal.zfill(max_len))

        pos = len(bin_start) - 1
        flips = 0

        for i in range(pos, -1, -1):
            if bin_start[i] != bin_goal[i]:
                flips += 1
                continue

        return flips

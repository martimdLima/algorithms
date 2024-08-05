class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] >= height:
                right[stack[-1]] = idx
                stack.pop()

            if stack:
                left[idx] = stack[-1]

            stack.append(idx)

        # Calculate the area for each rectangle by multiplying its
        # height (heights[i]) with the width calculated by subtracting
        # left[i] from right[i] and subtracting 1
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))

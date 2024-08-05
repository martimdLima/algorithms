from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # initialize left and right as both ends of the graph
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            # increment the left side if it's less than the right side and
            # the opposite if the right side is less than the left
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

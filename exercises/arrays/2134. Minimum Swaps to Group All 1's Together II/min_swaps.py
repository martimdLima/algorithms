from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length = len(nums)
        num_ones = nums.count(1)

        window_size = num_ones

        if length == 0 or window_size <= 0:
            return 0

        max_ones = sum(nums[i % length] for i in range(window_size))
        current_ones = max_ones

        for i in range(1, length):
            slide_out_element = nums[(i - 1) % length]
            slide_in_element = nums[(i + window_size - 1) % length]

            # current count of 1s in the window is updated by subtracting the
            # value of the element that has left the window and adding the
            # value of the new element that has entered.
            current_ones = current_ones - slide_out_element + slide_in_element
            max_ones = max(max_ones, current_ones)

        return num_ones - max_ones

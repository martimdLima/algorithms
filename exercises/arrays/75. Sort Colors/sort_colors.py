from Typing import List


class Solution:
    # using selection sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr_length = len(nums)

        for idx in range(0, arr_length):
            min_val = idx

            for jidx in range(idx + 1, arr_length):
                # update minimum value
                if nums[jidx] < nums[min_val]:
                    min_val = jidx

        # Swap only if a smaller element was found
        if min_val != idx:
            nums[idx], nums[min_val] = nums[min_val], nums[idx]

    # using bubble sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr_length = len(nums)

        for i in range(arr_length):
            # Last i elements are already in place
            for j in range(0, arr_length - i - 1):
                # Swap if the element found is greater than the next element
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # using insertion sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        arr_length = len(nums)

        if arr_length <= 1:
            return

        for i in range(1, arr_length):
            current_element = nums[i]
            j = i - 1  # previous element index
            while j >= 0 and current_element < nums[j]:
                nums[j + 1] = nums[j]  # shift elements to the right
                j -= 1
            nums[j + 1] = current_element

    # using merge sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge(left: List[int], right: List[int]) -> List[int]:
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        arr_length = len(nums)
        if arr_length <= 1:
            return

        mid = arr_length // 2
        left = nums[:mid]
        right = nums[mid:]

        self.sortColors(left)
        self.sortColors(right)

        sorted_arr = merge(left, right)

        nums[:] = sorted_arr

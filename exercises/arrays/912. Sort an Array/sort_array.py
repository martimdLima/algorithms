class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(left, right):
            # Base case: If the current segment is empty or has only one element, no need to sort.
            if left >= right:
                return

            # Choose a random pivot element from the segment.
            pivot = nums[randint(left, right)]

            # three-way partitioning
            less_than_pointer, greater_than_pointer, current = left - 1, right + 1, left

            current_is_greater_than_pointer = current < greater_than_pointer

            while current_is_greater_than_pointer:
                # Move the element to the segment with elements less or greater than pivot or continue to the next element if equal
                if nums[current] < pivot:
                    less_than_pointer += 1
                    nums[less_than_pointer], nums[current] = (
                        nums[current],
                        nums[less_than_pointer],
                    )
                    current += 1
                elif nums[current] > pivot:
                    greater_than_pointer -= 1
                    nums[greater_than_pointer], nums[current] = (
                        nums[current],
                        nums[greater_than_pointer],
                    )
                else:
                    current += 1

            # Recursively apply quick sort to the segment with elements less than and greater than pivot.
            quick_sort(left, less_than_pointer)
            quick_sort(greater_than_pointer, right)

        quick_sort(0, len(nums) - 1)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using the 3-way quick sort algorithm with random pivot selection.

        Args:
            nums (List[int]): The list of integers to sort.

        Returns:
            List[int]: The sorted list.
        """

        def partition_3way(arr: List[int], low: int, high: int) -> Tuple[int, int]:
            """
            Partitions the array into three parts: elements less than the pivot,
            elements equal to the pivot, and elements greater than the pivot.

            Args:
                arr (List[int]): The list of integers to partition.
                low (int): The starting index of the partition range.
                high (int): The ending index of the partition range.

            Returns:
                (int, int): The indices where the middle (equal to pivot) section starts and ends.
            """
            pivot_index = random.randint(low, high)
            pivot = arr[pivot_index]
            arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

            lt = low  # We initiate lt to be the part that is less than the pivot
            gt = high  # We initiate gt to be the part that is greater than the pivot
            i = low  # We scan the array from left to right

            while i <= gt:
                if arr[i] < pivot:
                    arr[lt], arr[i] = arr[i], arr[lt]
                    lt += 1
                    i += 1
                elif arr[i] > pivot:
                    arr[gt], arr[i] = arr[i], arr[gt]
                    gt -= 1
                else:
                    i += 1

            return lt, gt

        def quick_sort_recursive(arr: List[int], low: int, high: int) -> None:
            """
            Recursively applies the 3-way quick sort algorithm to the array.

            Args:
                arr (List[int]): The list of integers to sort.
                low (int): The starting index of the sort range.
                high (int): The ending index of the sort range.
            """
            if low < high:
                lt, gt = partition_3way(arr, low, high)
                quick_sort_recursive(arr, low, lt - 1)
                quick_sort_recursive(arr, gt + 1, high)

        quick_sort_recursive(nums, 0, len(nums) - 1)
        return nums

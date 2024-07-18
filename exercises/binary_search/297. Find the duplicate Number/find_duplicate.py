class Solution:
    # Binary Search approach
    def findDuplicate(self, nums: List[int]) -> int:
        def binary_search(input: list, target: int, start: int, end: int):
            while start <= end:
                mid = (start + end) // 2
                if input[mid] == target:
                    return mid
                elif input[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        nums.sort()

        i = 0
        while i < len(nums) - 1:
            target = nums[i]
            index = binary_search(nums, target, i + 1, len(nums) - 1)
            if index != -1:
                return nums[index]
            else:
                i += 1

        return 0

    # Binary Search approach
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        count = {}

        while left <= right:
            target = nums[left]
            if target not in count:
                count[target] = 1
            else:
                count[target] = count[target] + 1
                if count[target] == 2:
                    return target

            left += 1
        return 0

    # Hash Set approach
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

    # Floyd's Tortoise and Hare (Cycle Detection) approach
    def findDuplicate(nums: List[int]) -> int:
        # Phase 1: Finding the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Finding the entrance to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

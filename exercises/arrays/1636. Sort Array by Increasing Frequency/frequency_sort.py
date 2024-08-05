class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        nums_counter = Counter(nums)
        most_common = nums_counter.most_common()
        ascending = most_common[0][1] == 1

        freq = []

        if ascending:
            for key, val in most_common:
                freq += [key] * val
        else:
            for key, val in sorted(
                nums_counter.items(), key=lambda item: (-item[1], item[0]), reverse=True
            ):
                freq += [key] * val

        return freq

    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)

        # Sort elements based on frequency and then by value
        sorted_elements = sorted(nums_counter.items(), key=lambda x: (x[1], -x[0]))

        result = []
        for num, freq in sorted_elements:
            result.extend([num] * freq)

        return result

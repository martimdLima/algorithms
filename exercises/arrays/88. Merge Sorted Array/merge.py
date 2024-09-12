class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_size = len(nums1)
        for idx in range(nums1_size):
            if m == 1 and n == 0:
                return

            if m == 0 and n == 1:
                nums1[0] = nums2[0]
                return

            if idx >= m:
                nums1[idx] = nums2[idx - m]
        nums1.sort()

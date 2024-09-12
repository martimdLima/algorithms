class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]

                arr[i + 1] = 0

        print(arr)

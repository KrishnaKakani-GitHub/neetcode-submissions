from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: List[int], lo: int, mid: int, hi: int) -> None:
            left, right = arr[lo:mid + 1], arr[mid + 1:hi + 1]
            i, j, k = lo, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def merge_sort(arr: List[int], lo: int, hi: int) -> None:
            if lo >= hi:
                return
            mid = (lo + hi) // 2
            merge_sort(arr, lo, mid)
            merge_sort(arr, mid + 1, hi)
            merge(arr, lo, mid, hi)

        merge_sort(nums, 0, len(nums) - 1)
        return nums
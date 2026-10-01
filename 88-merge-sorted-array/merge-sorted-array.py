import sys

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = 0

        for i in range(m,m+n):
            nums1[i] = nums2[idx]
            idx += 1
        
        return nums1.sort()
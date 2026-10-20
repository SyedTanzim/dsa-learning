class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for i in range (len(nums1)):
            for j in range (len(nums2)):
                val = -1
                if nums2[j] == nums1[i]:
                    k = j+1
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            val = nums2[k]
                            break
                        k += 1

                    res.append(val)

        return res
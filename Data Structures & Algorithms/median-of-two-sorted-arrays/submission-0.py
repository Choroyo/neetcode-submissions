class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l = 0
        r = len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            nums1L = nums1[i] if i >= 0 else float("-infinity")
            nums1R = nums1[i + 1] if i + 1 < len(nums1) else float("+infinity")
            nums2L = nums2[j] if j >= 0 else float("-infinity")
            nums2R = nums2[j + 1] if j + 1 < len(nums2) else float("+infinity")

            if nums1L <= nums2R and nums2L <= nums1R:
                if total % 2 == 1:
                    median = min(nums1R, nums2R)
                else:
                    median = (max(nums1L, nums2L) + min(nums2R, nums1R)) / 2
                return median
            elif nums1L > nums2R:
                r = i - 1
            else:
                l = i + 1

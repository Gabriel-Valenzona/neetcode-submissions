class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_p, nums2_p = 0, 0

        while nums1_p < m and nums2_p < n:
            if nums1[nums1_p] < nums2[nums2_p]:
                nums1.insert(nums1_p, nums2[nums2_p])
        
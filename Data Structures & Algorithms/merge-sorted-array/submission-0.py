class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        num1_p, num2_p = 0, 0

        while num1_p < m and num2_p < n:
            if num1[num1_p] < num2[num2_p]:
                num1.insert(num1_p, num2[num2_p])
        
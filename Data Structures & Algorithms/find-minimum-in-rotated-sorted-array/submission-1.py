class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest_element = 0
        for num in nums:
            smallest_element = min(smallest_element, num)
        return smallest_element


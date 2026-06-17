class Solution:
    def findMin(self, nums: List[int]) -> int:
        first_element = nums[0] 
        for num in nums:
            if num < first_element: 
                smallest_element = num
        return smallest_element if smallest_element else 0


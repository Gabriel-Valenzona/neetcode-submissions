class Solution:
    def findMin(self, nums: List[int]) -> int:
        first_element = nums[0] 
        for num in nums:
            smallest_element = min(first_element, num)
            print(smallest_element)
        return smallest_element


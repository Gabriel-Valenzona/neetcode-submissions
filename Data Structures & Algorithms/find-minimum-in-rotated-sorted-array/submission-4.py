class Solution:
    def findMin(self, nums: List[int]) -> int:
        first_element = nums[0] 
        for num in nums:
            if num < first_element: 
                smallest_element = num
            print(smallest_element)
        return smallest_element


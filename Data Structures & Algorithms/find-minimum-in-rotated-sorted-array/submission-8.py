class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0] 
        for num in nums:
            if num < first_element: 
                min_val = num
        return min_val


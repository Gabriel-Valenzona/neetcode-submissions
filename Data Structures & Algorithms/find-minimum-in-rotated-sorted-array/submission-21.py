class Solution:
    def findMin(self, nums: List[int]) -> int:
        # approach: binary search on entire array, 
        # if mid is bigger than l, then it means mid is a part of the left pointer, meaning the minimum is not found yet 
        # if mid is smaller, then it means mid is not part of the left pointer, meaning the minimum is not found yet 
        nums = sorted(nums)

        if nums:
            return nums[0]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        index_to_insert = 0

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            if target > nums[l] and target < nums[l + 1]:
                index_to_insert = l
            elif target < nums[r] and target > nums[r - 1]:
                index_to_insert = r

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
        
        return index_to_insert

            

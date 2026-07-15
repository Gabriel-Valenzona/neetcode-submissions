class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        mid = l + (r - 1) // 2

        while l < r:
            if target > mid:
                l = mid + 1
            elif target < mid:
                r = mid - 1
            else:
                return mid
        
        return -1
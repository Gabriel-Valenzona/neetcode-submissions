class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > mid:
                l = mid + 1
            elif target < mid:
                r = mid - 1
            else:
                return mid
        
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)
            if target > nums[mid]:
                print(f"{l} before l increment")
                l = mid + 1
                print(f"{mid}" is mid)
                print(f"{l} after r increment")
            elif target < nums[mid]:
                print(f"{r} + before r increment")
                r = mid - 1
                print(f"{mid} + is mid")
                print(f"{r} + after r increment")
            else:
                return mid
        
        return -1
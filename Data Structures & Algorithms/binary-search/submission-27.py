class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            # target bigger than midpoint
            if nums[mid] < target:
                l = mid + 1
                print(f"t_b and {l}")
            # target smaller than midpoint
            elif nums[mid] > target:
                r = mid - 1
                print(f"t_s and {r}")
            # target found
            else:
                return mid
        
        return -1
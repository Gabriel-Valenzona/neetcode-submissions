class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + ((r - l) // 2)
            if target > nums[mid]:
                print(l + " before l increment")
                l = mid + 1
                print(mid + " is mid")
                print(l + " after r increment")
            elif target < nums[mid]:
                print(r + " before r increment")
                r = mid - 1
                print(mid + " is mid")
                print(r + " after r increment")
            else:
                return mid
        
        return -1
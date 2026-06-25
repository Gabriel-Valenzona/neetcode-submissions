class Solution:
    def findMin(self, nums: List[int]) -> int:
        # approach: binary search on entire array, 
        # if mid is bigger than l, then the minimum has been found
        # if mid is smaller than l, then the minimum has not been found yet since not sorted yet
 
        min_seen = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] < nums[r]: # means sorted
                min_seen = min(min_seen, nums[l])
                return min_seen

            mid = l + (r - l) // 2

            if nums[mid] > nums[r]: # if mid is bigger than l, then the minimum has been found
                l = mid + 1
            else:
                r = mid

        return nums[l]



                
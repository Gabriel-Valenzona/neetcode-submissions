class Solution:
    def findMin(self, nums: List[int]) -> int:
      res = nums[0]
      l, r = 0, len(nums) - 1

      while l <= r:

        mid_point = (l + r) // 2
        res = min(res, nums[mid_point])
        if nums[mid_point] >= nums[l]:
            l = mid_point + 1
        else:
            r = m - 1
    

        return res
        


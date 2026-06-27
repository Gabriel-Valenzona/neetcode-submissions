class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers - both. L pointer tracker where to place new R pointer (UNIQUE)
        l, r = 0, 1

        # move second pointer, compare to first, 
        while r < len(nums):
            # scenario 1: if right pointer unique (not duplicate), copy to L pointer, increment both pointers 
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
                r += 1
            # scenario 2: if right pointer not unique, keep left pointer same, right pointer increment
            else:
                r += 1
        
        return l + 1





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers - 1 on beginning, 2nd on second index

        # move second pointer, compare to first, 
            # scenario 1: if bigger, move left pointer up to right pointer, increment right pointer
            # scenario 2: if same (else), remove the left pointer value

        # return len(nums)

        l, r = 0, 1

        while l < len(nums):
            if nums[l] > nums[r]:
                l = r
                r += 1
            else:
                del nums[l]
        
        return len(nums)

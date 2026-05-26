class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # L AND R pointer to indicate left and right boundary of dynamic array
        L, R = 0, len(nums) - 1
        # loop that should terminate when pointers pass one another, 
        while L < R:
            # calculate mid-point
            mid_pointer = (L + R) // 2 # floor division because
            # check 1: if target > mid pointer value, make L = mid + 1... move up left pointer - shrinks window
            if target > nums[mid_pointer]:
                L = mid_pointer + 1
            # check 2: if target < mid pointer value, make R = mid - 1... adjust right pointer - shrinks window
                R = mid_pointer - 1
            # else: if target is neither bigger or smaller, then it means we have shrunk the window to a point only one index remains and its the desired target
                return nums[mid_pointer]
        # if we exit the loop (L becomes greater than R), then it means that there is no value found because that's the while-loop condition
        return -1
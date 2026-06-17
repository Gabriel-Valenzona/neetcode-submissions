class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init two pointers - L starts at first index, R start at right index: use these as bounds of possible index
        L, R = 0, len(nums) - 1
        # loop-condition: if L <= R pointer and nums
        while L <= R and nums:
            # init mid pointer = R - L // 2
            M = (R + L) // 2
            # if target value < M pointer
            if target < nums[M]:
                # change R pointer to M pointer location
                R = M - 1
            # if target value > M pointer
            elif target > nums[M]:
                # update L pointer to M pointer location
                L = M + 1
            # if target == M pointer value
            else:
                # return the index of the mid pointer
                return M
            print (L, M, R)
        
        return -1



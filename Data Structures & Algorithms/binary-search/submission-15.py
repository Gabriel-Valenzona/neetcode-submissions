class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            mid = l + (r - l) // 2
            # 3 scenarios
            if mid < target:
                r = mid - 1
                print(f'{r} + right')
            elif mid > target:
                l = mid + 1
                print(f'{l} + left')
            else:
                print(f'{mid} + left')
                return mid

        
        return -1
            
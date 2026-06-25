class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l<=r:
            mid = l + (r - l) // 2
            # 3 scenarios
            if target < mid:
                r = mid - 1
                print(r + 'right')
            elif target > mid:
                l = mid + 1
                print(l + 'left')
            else:
                print(mid + 'mid')
                return mid

        
        return -1
            
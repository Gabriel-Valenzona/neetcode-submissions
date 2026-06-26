class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. perform binary search to split array into two sorted halves
        2. perform binary search on left-side, if not found, perform on right
        3. either return the index if found or dsdsdsd†le
        '''
        l, r = 0, len(nums) - 1
        target_index = -1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[l]: # means sorted
                l = mid + 1
            else:
                r = mid - 1
        
        # left pointer becomes turning point

        # right-half array
        l_righth = l
        r_righth = len(nums) - 1

        # left-half array        
        l_lefth = 0
        r_lefth = r

        if target > nums[r_righth]:
            # loop through right sorted side
            while l_righth <= r_righth:
                mid = l_righth + (r_righth - l_righth) // 2
                
                if nums[mid] > target:
                    r_righth = mid - 1
                elif nums[mid] < target:
                    l_righth = mid + 1
                else:
                    target_index = mid
        else: 
            # loop through left sorted side
            while l_lefth <= r_lefth:
                mid = l_lefth + (r_lefth - l_lefth) // 2
                
                if nums[mid] > target:
                    r_lefth = mid - 1
                elif nums[mid] < target:
                    l_lefth = mid + 1
                else:
                    target_index = mid

        return target_index



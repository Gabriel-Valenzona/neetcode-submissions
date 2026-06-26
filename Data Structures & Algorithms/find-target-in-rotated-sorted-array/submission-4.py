class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1. perform binary search to split array into two sorted halves
        2. perform binary search on left-side, if not found, perform on right
        3. either return the index if found or dsdsdsd†le
        '''
        l, r = 0, len(nums) - 1

        while l < r: # WHY?
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]: # means pivot is to the right
                l = mid + 1
            else:
                r = mid
        
        # l pointer becomes turning point (index of the minimum element)

        # right-half array
        l_righth = l
        r_righth = len(nums) - 1

        # left-half array        
        l_lefth = 0
        r_lefth = r
        r_lefth = l - 1

        if target <= nums[len(nums) - 1]: # why??
            while l_righth <= r_righth:
                mid = l_righth + (r_righth - l_righth) // 2
                
                if nums[mid] > target:
                    r_righth = mid - 1
                elif nums[mid] < target:
                    l_righth = mid + 1
                else:
                    target_index = mid
                    return mid
            # loop through left sorted side
            while l_lefth <= r_lefth:
                mid = l_lefth + (r_lefth - l_lefth) // 2
                
                if nums[mid] > target:
                    r_lefth = mid - 1
                elif nums[mid] < target:
                    l_lefth = mid + 1
                else:
                    target_index = mid
                    return mid
        return -1



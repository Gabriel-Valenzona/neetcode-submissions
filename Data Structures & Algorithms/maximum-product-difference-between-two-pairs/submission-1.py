import heapq

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l = 0
        r = l + 1
        # loop through and compute as left and right pointer keeps going
        nums_heap = heapq.heapify(nums)

        product_max = 0
        nums_max = heapq.nlargest(2, nums_heap)
        product_max = nums_max[0] * nums_max[1]

        
        product_min = 0
        nums_min = heapq.nsmallest(2, nums_heap)
        product_min = nums_min[0] * nums_min[1]
        
        product_diff = product_max - product_min
        return product_diff 
            
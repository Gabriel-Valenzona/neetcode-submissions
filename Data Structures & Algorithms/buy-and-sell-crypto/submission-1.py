class Solution: 
    def maxProfit(self, prices: List[int]) -> int: 
        # l, r pointer
        l, r = 0, 1
        
        max_profit = 0

        # loop-condition: terminate when right pointer has nowhere else to go
        while r < len(prices):
            # init max_profit - store the biggest profit calculated
            # if selling price (smaller right pointer) is smaller than buying value (left pointer)
            if prices[l] < prices[r]:
                # calculate profit right pointer value (selling) - left pointer value (buying)
                profit = prices[r] - prices[l]
                # if its bigger than the max_profit found, then store that maximum value in the max_profit variable
                max_profit = max(max_profit, profit)
            # otherwise, move left pointer to right pointer location because we found a cheaper buy price
            else:
                l = r
                # move right pointer one index forward to the left
            r += 1
        
        return max_profit
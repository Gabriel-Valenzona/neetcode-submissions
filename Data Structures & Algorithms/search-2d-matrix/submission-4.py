class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init L and R pointer - to use once we find the specific row
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        # isolate the specific row w/ Binary Search
        while top <= bot: # breaks when no target found
            mid_row = (top + bot) // 2

            # target could be smaller than mid_row 
            if target < matrix[mid_row][0]:
                bot_row = mid_row - 1
            # target bigger than mid_row
            elif target > matrix[mid_row][-1]:
                top_row = mid_row + 1
            # target could be in row
            else:
                break

        # none found - return False
        if top > bot:
            return False

        # binary search over the row -- should calculate to same mid point
        mid_row = (top + bot) // 2
        
        # find specific target in range
        l, r = 0, COLS - 1
        while l <= r:
            mid =(l + r) // 2 
            if target > matrix[mid_row][mid]:
                l = mid + 1
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                return True

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[1]) # used to start first binary search

        # perform binary search over the rows to localize which row the target exists in
        top, bot = 0, len(ROWS) - 1
        while top <= bot:
            # calc mid point row
            mid_row = (top + bot) // 2
            # target > last index, then possible target location is at least in further rows
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            # target < first index, then possible target location is at least in previous rows
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            # if neither is executed, break because it either means row has been found because its target is within bounds of current row OR 
            else:
                break

        # if loop breaks becasue loop-condition rather than 'break' then it means there is no existing target
        if not (top <= bot):
            return False

        # once we find the row, perform a standard binary search on the row
        row_found = (top + bot) // 2
        l, r = 0, len(COLS)
        while l <= r:
            mid_point = (l + r) // 2
            if target > matrix[row_found][mid_point]:
                l = mid_point + 1
            elif target < matrix[row_found][mid_point]:
                r = mid_point - 1
            else:
                return True
        
        return False
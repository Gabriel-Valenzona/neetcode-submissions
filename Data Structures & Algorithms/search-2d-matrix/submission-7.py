class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            for c in matrix:
                if target == matrix[r][c]:
                    return True

        return False
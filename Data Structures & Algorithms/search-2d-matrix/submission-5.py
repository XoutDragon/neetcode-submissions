class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ml = len(matrix)
        mil = len(matrix[0])

        def get_r_c(idx):
            return idx // mil, idx % mil

        start = 0 
        end = ml * mil - 1

        while start <= end:
            half = (start + end) >> 1

            r, c = get_r_c(half)

            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] < target:
                start = half + 1
            else:
                end = half - 1

        return False
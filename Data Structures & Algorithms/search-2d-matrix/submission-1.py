class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchList(l: List[int], target: int) -> bool:
            if target < l[0] or target > l[len(l) - 1]:
                return False
            
            i = len(l) // 2

            if l[i] == target:
                return True
            
            if len(l) == 1:
                return False

            return searchList(l[i+1:], target) if target > l[i] else searchList(l[0: i], target)
        
        for i in range(len(matrix)):
            if searchList(matrix[i], target):
                return True

        return False
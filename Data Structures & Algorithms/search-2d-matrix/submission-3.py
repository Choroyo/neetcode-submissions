class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        topR, botR = 0, rows - 1
        while topR <= botR:
            midR = (topR + botR) // 2
            if matrix[midR][-1] < target:
                totR = midR + 1
            elif matrix[midR][0] > target:
                botR = midR - 1
            else:
                break
        if not topR <= botR:
            return False
        
        row = (topR + botR) // 2
        start, end = 0, cols - 1

        while start < end:
            mid = (start + end) // 2

            if matrix[start][mid] == target:
                return True
            if matrix[start][mid] < target:
                start = mid + 1
            elif matrix[start][mid] > target:
                end = mid - 1
        return False



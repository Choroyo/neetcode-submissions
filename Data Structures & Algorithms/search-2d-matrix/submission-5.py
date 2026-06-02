class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        topR, botR = 0, rows - 1
        while topR <= botR:
            midR = (topR + botR) // 2
            if matrix[midR][-1] < target:
                topR = midR + 1
            elif matrix[midR][0] > target:
                botR = midR - 1
            else:
                break
        print(topR, botR)
        if not topR <= botR:
            print("here")
            return False
        
        row = (topR + botR) // 2
        print(row)
        start, end = 0, cols - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                return True
        return False



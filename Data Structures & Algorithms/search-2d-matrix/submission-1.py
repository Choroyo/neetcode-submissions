def binarySearch(matrix: List[List[int]], target: int, start: tuple, end: tuple) -> bool:
    if ((startR == endR and startC > endC) or (startR > endR)):
        return False
    
    startR = start[0]
    startC = start[1]

    endR = end[0]
    endC = end[1]

    midR = (startR + endR) // 2
    midC = (startC + endC) // 2
    
    if matrix[midR][midC] == target:
        return True
    
    if matrix[midR][midC] > target:
        if midC == 0:
            midR = midR - 1
            midC = len(matrix[0]) - 1
        else:
            midC = midC - 1
        return binarySearch(matrix, target, start, (midR, midC))

    if matrix[midR][midC] < target:
        if midC == len(matrix[0]) - 1:
            midR = midR + 1
            midC = 0
        else:
            midC = midC + 1
        return binarySearch(matrix, target, (midR, midC), end)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = (0,0)
        end = (len(matrix) - 1, len(matrix[0]) - 1)
        
        return binarySearch(matrix, target, start, end)

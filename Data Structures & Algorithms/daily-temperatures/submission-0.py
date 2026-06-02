class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                stackI, stackJ = stack.pop()
                result[stackJ] = i - stackJ
            stack.append((j, i))
        return result
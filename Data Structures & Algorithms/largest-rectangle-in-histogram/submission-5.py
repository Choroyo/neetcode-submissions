class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        index = 0

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
                continue

            if heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
            else:
                while stack and heights[i] < stack[-1][1]:
                    index = stack[-1][0]
                    area = stack[-1][1] * (i - index)
                    maxArea = max(maxArea, area)
                    stack.pop()
                stack.append([index, heights[i]])

        while stack:
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            maxArea = max(maxArea, area)
            stack.pop()

        return maxArea
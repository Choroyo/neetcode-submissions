class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = max(heights)

        stack = []

        for i in range(len(heights)):
            if not stack:
                stack.append([i, heights[i]])
                print(stack, 0)
                continue
            if heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
                print(stack , 1)
            else:
                while heights[i] < stack[-1][1]:
                    index = stack[-1][0]
                    
                    area = stack[-1][1] * (i - index)
                    maxArea = max(maxArea, area)

                    stack.pop()
                    stack.append([index, heights[i]])
                    print(heights[i], stack[-1][1])
                    print(stack, 2)
                    print(maxArea)

        while stack:
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            maxArea = max(maxArea, area)
            stack.pop()
            print(maxArea)

        return maxArea
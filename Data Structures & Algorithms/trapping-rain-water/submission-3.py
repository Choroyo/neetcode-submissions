class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        maxArea = 0
        while r < len(height):
            print(height[l], height[r])
            if height[l] > height [r]:
                r += 1
                print("here 1: new height[r] = " + str(height[r - 1]))
            elif height[r] > height[l]:
                negArea = 0
                for i in range(l + 1, r - 1):
                    negArea += height[i]
                    print(negArea, height[i])
                area = (min(height[l], height[r]) * (r - l - 1)) - negArea
                maxArea += area
                l = r
                r += 1
                print("here 2: ", str(area), str(maxArea), str(negArea))
            elif height[r] == height[l]:
                negArea = 0
                for i in range(l + 1, r):
                    negArea += height[i]
                    print(height[i])
                area = (min(height[l], height[r]) * (r - l - 1)) - negArea
                maxArea += area
                l = r
                r += 1
                print("here 3: ", str(area), str(maxArea), str(negArea))
        return maxArea
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = 1
        maxArea = 0
        while r < len(height):
            print(height[l], height[r])
        
            if height[r - 1] < height[r]:
                negArea = 0
                for i in range(l + 1, r - 1):
                    negArea += height[i]
                area = min(height[l], height[r]) * (r - l - 1)
                if area > maxArea:
                    maxArea = area
                print("here 1: " + str(area), str(maxArea))
            if height[l] > height [r]:
                r += 1
                print("here 2: " + str(r))
            elif height[r] > height[l]:
                l = r
                r += 1
                print("here 3: " + str(l), str(r))
            elif height[r] == height[l]:
                l = r
                r += 1
                print("here 4: " + str(l), str(r))
            else:
                r += 1
        return maxArea
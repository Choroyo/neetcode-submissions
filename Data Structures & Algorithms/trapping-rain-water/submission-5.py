class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lMax= 0
        rMax = 0
        maxArea = 0

        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            if height[l] > height [r]:
                r -= 1
                area = min(lMax, rMax) - height[r]
                if area > 0:
                    maxArea += area
            elif height[l] < height[r]:
                l += 1
                area = min(lMax, rMax) - height[l]
                if area > 0:
                    maxArea += area
            elif height[r] == height[l]:
                l += 1
                area = min(lMax, rMax) - height[l]
                if area > 0:
                    maxArea += area
        return maxArea
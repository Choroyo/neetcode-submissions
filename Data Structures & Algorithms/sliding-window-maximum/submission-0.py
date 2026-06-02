class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        l = 0
        r = k

        while r < len(nums) + 1:
            result.append(max(nums[l:r]))
            r += 1
            l += 1
        
        return result
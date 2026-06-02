class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 1
        while i < len(nums) :
            print(i)
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            i += nums[i]
        return True

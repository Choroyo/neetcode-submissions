class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if nums[i] in sums:
                return [sums[nums[i]],i]
            sums[need] = i
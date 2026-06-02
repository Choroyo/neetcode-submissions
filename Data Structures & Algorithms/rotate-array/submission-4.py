class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)

        print(nums[-steps:] , nums[:-steps]) 
        print(nums[steps:] , nums[:steps])    

        nums[:] = nums[steps:] + nums[:-steps]     

        print(nums[-steps:] , nums[:-steps]) 
        print(nums[steps:] , nums[:steps])           
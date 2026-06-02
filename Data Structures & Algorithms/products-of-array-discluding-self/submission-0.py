class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for i in range(len(nums)):
            product *= nums
            prefix.append(product)
        
        print(prefix)
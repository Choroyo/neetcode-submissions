class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        postfix = []

        product = 1

        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)
        print(prefix)
        product = 1        
        for i in range(len(nums) - 1,-1, -1):
            product *= nums[i]
            postfix.append(product)
        
        postfix = postfix[::-1]
        print(postfix)
        result = []
        result.append(postfix[1])
        for i in range(len(nums) - 2):
            result.append(prefix[i] * postfix[i + 2])
        result.append(prefix[-2])

        return result
        print(postfix)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numList = []

        for num in nums:
            if num in numList:
                return True
            numList.append(num)
        return False
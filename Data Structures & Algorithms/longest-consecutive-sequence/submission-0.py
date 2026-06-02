class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        startNums = set()
        
        result = 0

        for num in nums:
            if num - 1 not in nums:
                startNums.add(num)

        for val in startNums:
            count = 1
            number = val + 1

            while True:
                if number in setNums:
                    count += 1
                else:
                    break
                number += 1

            if count > result:
                result = count
        return result

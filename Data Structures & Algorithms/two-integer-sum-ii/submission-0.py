class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = 1
        result = []
        while r < len(numbers) : 
            num = target - numbers[l]
            if numbers[r] == num:
                result.append(l + 1)
                result.append(r + 1)
                return result

            if numbers[r] > num:
                l += 1
            r += 1 


        
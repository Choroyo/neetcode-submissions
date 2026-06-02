class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        result = []
        while l < r  : 
            num = target - numbers[l]
            print(num, l, r)
            if numbers[r] == num:
                result.append(l + 1)
                result.append(r + 1)
                return result

            if numbers[r] > num:
                r -= 1
            else:
                l += 1 


        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        countFreq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            frequency[num] = 1 + frequency.get(num,0)
        for num, count in frequency.items():
            countFreq[count].append(num)
        
        result = []
        for i in range(len(countFreq) - 1, 0, -1):
            for n in countFreq[i]:
                result.append(n)
                if len(result) == k:
                    return result

            
        
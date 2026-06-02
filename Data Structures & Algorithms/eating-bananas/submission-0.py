class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        k = [x for val in range(1, end + 1)]

        print(k)

        return 0
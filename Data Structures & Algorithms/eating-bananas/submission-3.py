class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)

        minK = end

        while start <= end:
            mid = (start + end) // 2
            hours = 0
            for elem in piles:
                hours += math.ceil(elem / mid) 
            if hours <= h:
                end = mid - 1
                if mid < minK:
                    minK = mid 
            elif hours > h:
                start = mid + 1
        return minK
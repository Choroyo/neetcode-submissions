class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        mapCount = {}
        result = 0
        maxF = 0
        for r in range(len(s)):
            mapCount[s[r]] = mapCount.get(s[r], 0) + 1
            maxF = max(maxF, mapCount[s[r]])

            while sum(mapCount.values()) - maxF > k:
                mapCount[s[l]] -= 1
                l += 1
            result = max(result, sum(mapCount.values()))
        return result
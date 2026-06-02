class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        mapCount = {}
        result = 0
        replace = 0
        while r < len(s):
            print(replace)
            print(result)
            if replace <= k:
                mapCount[s[r]] = mapCount.get(s[r], 0) + 1
                replace = sum(mapCount.values()) - (max(mapCount.values()))
                if replace <= k:
                    result = max(result, sum(mapCount.values()))
                print("here")
            else:
                print("here 2")
                mapCount[s[l]] = mapCount[s[l]] - 1
                l += 1
            r += 1
            print(mapCount)
        return result
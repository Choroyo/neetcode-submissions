class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = {}
        dicS = {}
        r = 0
        l = 0
        result = ""
        minLen = len(s)
        match = 0
    
        for char in t:
            dicT[char] = dicT.get(char, 0) + 1

        for char in t:
            dicS[char] = dicS.get(char, 0)

        need = sum(dicT.values())
        while r < len(s):
            if s[r] in dicT:
                dicS[s[r]] = dicS.get(s[r], 0) + 1
                if dicS[s[r]] <= dicT[s[r]]:
                    match += 1
                    print(match)
                    print(result)
            
            while match == need:
                if len(s[l: r + 1]) <= minLen:
                    minLen = len(s[l:r + 1])
                    result = s[l:r + 1]

                if s[l] in dicT:
                    dicS[s[l]] -= 1
                    if dicS[s[l]] < dicT[s[l]]:
                        match -= 1
                l += 1
            r += 1

        return result   

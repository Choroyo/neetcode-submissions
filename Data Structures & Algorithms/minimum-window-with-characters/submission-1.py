class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT = {}
        dicS = {}
        r = 0
        l = 0
        result = ""
        minLen = len(s)

        for char in t:
            dicT[char] = dicT.get(char, 0) + 1

        for char in t:
            dicS[char] = dicS.get(char, 0)

        while r < len(s):
            match = 0
            if s[r] in dicT:
                dicS[s[r]] = dicS.get(s[r], 0) + 1
            
            for elem in dicT:
                if dicS[elem] >= dicT[elem]:
                    match += 1

            while match == len(dicT):
                if len(s[l:r + 1]) <= minLen:
                    minLen = len(s[l:r + 1])
                    result = s[l:r + 1]
                    print(result)
                if s[l] in dicS:
                    dicS[s[l]] -= 1
                    if dicS[s[l]] < dicT[s[l]]:
                        match -= 1
                l += 1
            r += 1

        return result   

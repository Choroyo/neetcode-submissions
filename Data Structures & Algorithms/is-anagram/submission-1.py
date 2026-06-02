class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letterInS = {}
        letterInT = {}
        for c in s:
            if c in letterInS:
                letterInS[c] += 1
            else:
                letterInS[c] = 1
        print(letterInS)

        for c in t:
            if c in letterInT:
                letterInT[c] += 1
            else:
                letterInT[c] = 1

        for c in letterInS:
            if c in letterInT:
                if letterInT[c] != letterInS[c]:
                    return False
            else: 
                return False
                
        for c in letterInT:
            if c in letterInS:
                if letterInS[c] != letterInT[c]:
                    return False
            else: 
                return False

        return True 
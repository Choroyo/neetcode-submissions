class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs:
            string = ""
            i = 0
            while i < len(strs) - 1:
                string += (strs[i] + "#")
                i += 1
            string += strs[i]
            return string
        return strs[0]
    def decode(self, s: str) -> List[str]:
        if s:
            decodeList = s.split("#")
            return decodeList
            print(decodeList)
        return [s]
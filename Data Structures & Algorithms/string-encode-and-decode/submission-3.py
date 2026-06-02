class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        if strs:
            i = 0
            while i < len(strs) - 1:
                string += (strs[i] + "#")
                i += 1
            string += strs[i]
        return string
    def decode(self, s: str) -> List[str]:
        decodeList = s.split("#")
        print(decodeList)
        return decodeList
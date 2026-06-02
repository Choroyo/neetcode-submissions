class Solution:
    def encode(self, strs: List[str]) -> str:
        if strs:
            string = ""
            i = 0
            while i < len(strs) - 1:
                string += (strs[i] + "#")
                i += 1
            string += strs[i]
            print("inside")
            return string
            print("outside")
        return str(strs)
    def decode(self, s: str) -> List[str]:
        if s:
            decodeList = s.split("#")
            print(decodeList)
            return decodeList
        return list(s)
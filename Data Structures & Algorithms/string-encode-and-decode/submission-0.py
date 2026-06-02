class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += (s + "#")
        print(string)
        return string
    def decode(self, s: str) -> List[str]:
        return strs
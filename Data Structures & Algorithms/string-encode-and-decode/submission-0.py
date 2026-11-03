class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "%"
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            
            while s[i] != "%":
                length += s[i]
                i += 1
            i += 1
            res.append(s[i:int(length)+i])
            i += int(length) 
        
        return res
        
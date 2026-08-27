class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded = encoded + str(len(s)) + '#' + s
        return encoded    

    def decode(self, s: str) -> List[str]:
        res = []

        length = ''
        i = 0
        while i < len(s):
            if s[i] in {'1','2','3','4','5','6','7','8','9','0'}:
                length += s[i]
                i += 1
            if s[i] == '#':
                i += 1
                buffer = s[i: i + int(length)]
                i += int(length)
                res.append(buffer)
                length = ''
                continue
        return res
        

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        max_len = 0
        characters = set()
        while r < len(s):
            if s[r] in characters:
                while s[r] in characters: 
                    characters.remove(s[l])
                    l += 1
            characters.add(s[r])
            r += 1
            max_len = max(max_len, len(characters))
        return max_len

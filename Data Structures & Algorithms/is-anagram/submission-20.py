class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_map_1 = {}
        for i, c in enumerate(s):
           freq_map_1[c] = freq_map_1.get(c, 0) + 1
        
        freq_map_2 = {}
        for i, c in enumerate(t):
            freq_map_2[c] = freq_map_2.get(c, 0) + 1
        
        if freq_map_1 == freq_map_2:
            return True
        else:
            return False
            

            

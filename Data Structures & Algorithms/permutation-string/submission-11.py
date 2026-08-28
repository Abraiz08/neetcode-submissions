class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        a1 = [0]*26
        a2 = [0]*26

        for i in range(len(s1)):
            a1[ord(s1[i])-ord('a')] += 1
            a2[ord(s2[i])-ord('a')] += 1
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            if a1 == a2:
                return True 
            else:
                a2[ord(s2[l])-ord('a')] -= 1
                l += 1
                if r + 1 >= len(s2):
                    return False
                r+=1
                a2[ord(s2[r])-ord('a')] += 1
        return False
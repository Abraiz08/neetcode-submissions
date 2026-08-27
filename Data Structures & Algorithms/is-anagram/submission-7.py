class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: all the characters are the same
        # what can i hash? cant have characters as keys since they can repeat
        # can i add a counter to the value everytime? then i cant have early exit, lets try this way
        
        countS, countT = {},{}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        return countS == countT
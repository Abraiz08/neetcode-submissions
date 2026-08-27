class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: all the characters are the same
        # what can i hash? cant have characters as keys since they can repeat
        # can i add a counter to the value everytime? then i cant have early exit, lets try this way
        
        
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)
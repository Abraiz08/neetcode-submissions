class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram: all the characters are the same
        # what can i hash? cant have characters as keys since they can repeat
        # can i add a counter to the value everytime? then i cant have early exit, lets try this way
        my_dict = {}

        if len(s) != len(t):
            return False

        for i, char in enumerate(s):
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        
        for i, char in enumerate(t):
            if char in my_dict:
                my_dict[char] -= 1
            else: 
                return False
        
        for value in my_dict.values():
            if value != 0:
                return False
        
        return True
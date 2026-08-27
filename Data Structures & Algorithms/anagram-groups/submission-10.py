class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            freq = [0]*26
            for char in s:
                freq[ord(char)-97] += 1
            my_dict[tuple(freq)].append(s)

        return list(my_dict.values())



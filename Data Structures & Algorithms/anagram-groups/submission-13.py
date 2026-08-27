class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for i, s in enumerate(strs):
            arr = [0]*26
            for c in s:
                arr[ord(c)-97] += 1
            my_dict[tuple(arr)].append(s)
        res = []
        return list(my_dict.values())

        
            
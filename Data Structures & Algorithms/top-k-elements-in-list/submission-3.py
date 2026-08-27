from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count2 = count.most_common()
        res = []
        i = 0
        for key in count2:
            res.append(count2[i][0])
            i += 1
            if i == k:
                break
        return res
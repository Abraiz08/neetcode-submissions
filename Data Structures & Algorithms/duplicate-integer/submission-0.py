class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_to_index = {}
        for i, num in enumerate(nums):
            if num in num_to_index:
                return True
            num_to_index[num] = i
        return False
            
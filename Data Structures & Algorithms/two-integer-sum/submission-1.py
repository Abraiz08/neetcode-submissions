class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two integers in array should add up to target
        # in map, store the complement as key and index as position
        complement_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if num in complement_to_index:
                return [complement_to_index[num], i]
            complement_to_index[complement] = i
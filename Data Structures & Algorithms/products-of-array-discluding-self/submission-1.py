class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        i = 1
        while i < len(nums):
            prefix.append(nums[i-1]*prefix[i-1])
            i += 1

        suffix = [1]
        j = len(nums)
        i = 1
        while j > 1:
            suffix.append(nums[j-1]*suffix[i-1])
            j -= 1
            i += 1
        
        res = []
        i = 0
        while i < len(nums):
            res.append(prefix[i]*suffix[len(nums)-1-i])
            i+=1

        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # one number can sit in a buffer while i two pointer my way through the rest of the list
        checked = set()
        buffer = 0
        res = []
        res_set = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            buffer = nums[i]
            checked.add(i)
            l = i
            r = len(nums) - 1
            while l < r:
                if l in checked:
                    l += 1
                    continue
                if r in checked:
                    r -= 1
                    continue
                if buffer + nums[l] + nums[r]  == 0:
                    if tuple([buffer, nums[l], nums[r]]) not in res_set:
                        res.append([buffer, nums[l], nums[r]])
                        res_set.add(tuple([buffer, nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif buffer + nums[l] + nums[r]  > 0:
                    r -= 1
                elif buffer + nums[l] + nums[r]  < 0:
                    l += 1

        return res


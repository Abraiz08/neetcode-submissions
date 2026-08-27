class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums_sorted = sorted(nums)
        
        for i in range(len(nums_sorted)-2):
            if i > 0 and nums_sorted[i] == nums_sorted[i-1]:
                continue
            j = i+1
            k = len(nums_sorted)-1

            while j < k:
                curSum = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if curSum != 0:
                    if curSum > 0:
                        k -= 1
                    elif curSum < 0:
                        j += 1
                else:
                    result_list.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    while j < k and nums_sorted[j] == nums_sorted[j+1]:
                        j += 1
                    while j < k and nums_sorted[k] == nums_sorted[k-1]:
                        k -= 1
                    k -= 1
                    j += 1

        return result_list
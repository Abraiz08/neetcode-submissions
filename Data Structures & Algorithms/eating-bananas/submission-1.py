import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        mink = 1
        maxk = max(piles)
       
        curr_min = math.inf
        while mink <= maxk:
            k = (maxk + mink)//2
            print(mink, maxk, k)
            total_hours = 0
            for i in range(len(piles)):
                total_hours += math.ceil(piles[i] / k)
            if total_hours <= h:
                curr_min = min(curr_min, k)
                maxk = k - 1 
            if total_hours > h:
                mink = k + 1

        return curr_min
            

                

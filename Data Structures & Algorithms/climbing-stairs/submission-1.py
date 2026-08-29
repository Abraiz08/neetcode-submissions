class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(curr: int) -> int:
            # Base cases
            if curr > n:
                return 0
            if curr == n:
                return 1
            
            # Check cache before doing work
            if curr in memo:
                return memo[curr]

            # Compute, cache, and return
            memo[curr] = climb(curr + 1) + climb(curr + 2)
            return memo[curr]

        return climb(0)
        
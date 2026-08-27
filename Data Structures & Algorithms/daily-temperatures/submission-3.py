class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #i is where we at
        #index is what you pop
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures) - 1):
            stack.append(i)
            i += 1
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i - index
           
        return result

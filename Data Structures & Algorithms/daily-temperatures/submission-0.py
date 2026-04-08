class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][1]:
                i_popped, _ = stack.pop()
                res[i_popped] = i - i_popped
            stack.append((i,tmp))
        return res
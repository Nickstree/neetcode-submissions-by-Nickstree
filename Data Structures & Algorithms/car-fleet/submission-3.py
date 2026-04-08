class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        stack = []
        for i in range(len(position)):
            time.append((target - position[i]) / speed[i])
        position_time = list(zip(position, time))
        position_time = sorted(position_time, key = lambda x: x[0], reverse=True)
        for car in position_time:
            if not stack or car[1] > stack[-1][1]:
                stack.append(car)
            else:
                continue
        return len(stack)
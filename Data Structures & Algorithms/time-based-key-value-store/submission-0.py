class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.time_map[key]
        if not data:
            return ""
        l, r = 0, len(data) - 1
        while l <= r:
            m = l + (r - l) // 2
            if timestamp < data[m][1]:
                r = m - 1
            elif timestamp > data[m][1]:
                l = m + 1
            else:
                return data[m][0]
    
        return "" if r < 0 else data[r][0]

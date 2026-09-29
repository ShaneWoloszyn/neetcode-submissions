class TimeMap:

    def __init__(self):
        # hashmap {key:[value, timestamp]}
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key] = []
        
        self.tMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        
        row = self.tMap[key]

        l, r = 0, len(row) - 1

        res = ""

        while l <= r:
            m = (l + r) // 2

            if row[m][0] <= timestamp:
                res = row[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
        

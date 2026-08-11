class LRUCache:

    def __init__(self, capacity: int):
        self.keyMap = {}
        self.cap = capacity
        self.t = 0
        

    def get(self, key: int) -> int:
        self.t += 1
        if key in self.keyMap:       
            self.keyMap[key][1] = self.t
            return self.keyMap[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        self.t += 1
        self.keyMap[key] = [value, self.t]
        curMin = self.t
        res = -1
        if len(self.keyMap) > self.cap:
            print(self.keyMap, res, curMin)
            for key, val in self.keyMap.items():
                print(val)
                if val[1] < curMin:
                    res = key
                    curMin = val[1]

            del self.keyMap[res]
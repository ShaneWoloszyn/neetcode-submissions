class LRUCache:

    def __init__(self, capacity: int):
        self.keys = []
        self.vals = []
        self.cap = capacity

    def get(self, key: int) -> int:

        if key not in self.keys:
            return -1
        
        idx = self.keys.index(key)
        val = self.vals.pop(idx)
        self.keys.pop(idx)
        self.vals.append(val)
        self.keys.append(key)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            idx = self.keys.index(key)
            self.vals.pop(idx)
            self.keys.pop(idx)
            self.keys.append(key)
            self.vals.append(value)
            return
        
        if len(self.keys) == self.cap:
            self.keys.pop(0)
            self.vals.pop(0)
            self.keys.append(key)
            self.vals.append(value)
            return
        
        self.keys.append(key)
        self.vals.append(value)

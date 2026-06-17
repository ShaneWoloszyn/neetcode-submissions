class LRUCache:

    def __init__(self, capacity: int):
        self.nMap = {}
        self.fifo = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.nMap:
            self.fifo.pop(self.fifo.index(key))
            self.fifo.append(key)
            return self.nMap[key]       
        return -1

    def put(self, key: int, value: int) -> None:
        # if its full
        if key in self.nMap:
            self.nMap[key] = value
            self.fifo.pop(self.fifo.index(key))
            self.fifo.append(key)
            return
        
        if len(self.fifo) == self.cap:
            # delete the oldest from map
            del self.nMap[self.fifo.pop(0)]
            # append the newest key
            self.fifo.append(key)
            # add newest to map
            self.nMap[key] = value
            return
        
        # not full
        self.fifo.append(key)
        self.nMap[key] = value


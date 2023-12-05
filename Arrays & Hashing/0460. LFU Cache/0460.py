class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = defaultdict(int)
        self.min_freq = float('inf')
        self.frequencies = defaultdict(lambda: OrderedDict())

    def get(self, key: int) -> int:
        f = self.values[key] # get the frequency
        
        if not f:
            del self.values[key]
            return -1
        
        self.frequencies[f + 1][key] = self.frequencies[f][key]
        self.values[key] = f + 1

        del self.frequencies[f][key]

        if self.min_freq == f and len(self.frequencies[f]) == 0:
            self.min_freq = f + 1
        
        return self.frequencies[f + 1][key]
                        
    def put(self, key: int, value: int) -> None:
        
        if len(self.values) == self.capacity:
            if not self.values[key]:
                k = self.frequencies[self.min_freq].popitem(last=False) # FIFO --> first in first out (queue) (LRU)
                del self.values[k[0]]

        f = self.values[key]
        self.values[key] += 1

        if f != 0:
            self.frequencies[f + 1][key] = value
            del self.frequencies[f][key]
            
            if self.min_freq == f and len(self.frequencies[f]) == 0:
                self.min_freq = f + 1
        else:
            self.frequencies[f + 1][key] = value

        self.min_freq = min(self.values[key], self.min_freq)


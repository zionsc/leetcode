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
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = defaultdict(int)
        self.min_freq = float('inf')
        self.frequencies = defaultdict(lambda: OrderedDict())

    def get(self, key: int) -> int:
        


    def put(self, key: int, value: int) -> None:
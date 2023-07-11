class TimeMap:
    def __init__(self):
        # use defaultdict to initialize all non-initialized values as empty lists
        self.storage = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        # for each key, add [value, timestamp] pair to it (append)
        self.storage[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:


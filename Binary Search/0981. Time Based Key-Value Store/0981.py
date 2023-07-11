class TimeMap:
    def __init__(self):
        # use defaultdict to initialize all non-initialized values as empty lists
        self.storage = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        # for each key, add [value, timestamp] pair to it (append)
        self.storage[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        res = "" # res is initialized to an empty list in order to make sure that it is simply returned if not found in keys
        values = self.storage.get(key, []) # values = storage[key]'s list of pairs. Else it returns an empty list []

        m = l + ((r - l) // 2)

        while l <= r:
            if values[m] <=


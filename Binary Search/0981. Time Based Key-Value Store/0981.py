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

        # Binary Search for valid timestamp!

        l, r = 0, len(values) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][1] <= timestamp: # if it is a valid timestamp (less than or equal to timestamp at values[m]) -> values[m][1] is timestamp of values[m]
                res = values[m][0] # res is updated to the most recent valid timestamp (most close to but less than or equal to given input timestamp)
                l = m + 1 # update the binary search, keep searching for more valid timestamps! (most close to but less than or equal to the given input timestamp)
                # search right side now
            else: # not a valid timestamp --> larger than given input timestamp
                r = m - 1 # search left-side now 
        
        return res


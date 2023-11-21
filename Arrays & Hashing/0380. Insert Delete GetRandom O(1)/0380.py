class RandomizedSet: # hashmap val:index_in_list (in order to remove from list) | list = value

    def __init__(self):
        self.my_map = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool: 
        if val in self.my_map:
            return False
        self.arr.append(val)
        self.my_map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool: 
        if val not in self.my_map:
            return False
        # since we need to maintain the indexes in the array, we need to make sure to pop the last value.
        #  --> change the last value and the value we want to pop in both data structures.
        idx = self.arr[self.my_map[val]]

        self.my_map[self.arr[-1]] = idx
        self.arr[idx] = self.arr[-1]

        self.arr.pop()
        self.my_map.pop(val)

        return True
    
    def getRandom(self) -> int:
        return random.choice(self.arr)
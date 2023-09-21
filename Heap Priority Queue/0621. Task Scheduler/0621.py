class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # basically gives me a hashmap [character, number of occurences within tasks]
        count = Counter(tasks)
        
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_map = Counter(arr1)
        res = []
        remaining = []

        for num in arr2:
            for _ in range(arr1_map[num]):
                res.append(num)
                arr1_map[num] -= 1
        for num, freq in arr1_map.items():
            for _ in range(freq):
                remaining.append(num)

        remaining.sort()
        res.extend(remaining)
        return res
    
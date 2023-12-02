class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(length)]

        for start, end, inc in updates:
            arr[start] += inc

            if end + 1 < length:
                # this basically cancels out the prefix sum after end. This is because we dont want to inc
                # after the range start:end
                arr[end + 1] -= inc
            
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]

        return arr

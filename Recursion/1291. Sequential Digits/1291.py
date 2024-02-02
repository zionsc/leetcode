class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        # so basically create al the numbers that start with 1 was the leftmost number,2,3,4,5,6,7,8,9 --> then sort.
        # 123,1234,12345, 234,2345,23456, etc

        res = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                if low <= num <= high:
                    res.append(num)
                next_digit += 1

        return sorted(res)
// Bottom up Dynamic Programming Solution

// if n = 3 --> 0 1 2 3 (3 = 1 way, 2 = 1 way. 1 = 2(way) + 3(way) = 2, 0 = 1(way) + 2(way) = 3(way))

class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        
        if (n == 2) {
            return 2;
        }

        int one = 1, two = 1;

        for (int i = 0; i < n-1; ++i) {
            int temp = one;
            one = one + two;
            two = temp;
        }

        return one;
    }
};
class Solution:
    def numberOfWays(self, rats: str) -> int:
        # edge case
        num_rats = 0
        for i in range(len(rats)):
            if rats[i] == 'S':
                num_rats += 1
        if num_rats < 2:
            print("hello")
            return 0

        MOD = 10**9 + 7
        res = 1

        chairs = 0
        pots = 0
        for i in range(len(rats)):
            if rats[i] == 'P':
                pots += 1
            if rats[i] == 'S':
                if chairs % 2 == 0 and chairs != 0:
                    print(pots)
                    res *= (pots + 1)
                    res %= MOD
                    pots = 0
                    chairs += 1
                else: # chairs % 2 == 1
                    pots = 0
                    chairs += 1

        if chairs % 2 == 1:
            return 0

        return res % MOD

        
            


            
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate the time it takes for each car to reach the destination from len(position) - 1 (backwards) as cars change speed to their front car
        # thus we don't know what speed the cars are going in unless we iterate backwards (target - position) / speed --> time it takes to get to target
        # must have sorted positions in order to do this as we need it to determine backwards in relation to the position
        
        # creating a list of pairs --> must do this as we cannot sort the pos and speed lists in the same order, but separately.
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p , s in sorted(pair, reverse=True: # or I can do [::-1]
            stack.append((target - p) / s)

            # if the car behind the front car has a faster time to reach the target, then it will become one fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)